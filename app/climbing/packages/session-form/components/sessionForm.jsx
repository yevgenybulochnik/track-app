import React from 'react'
import axios from 'axios';

import {ButtonInput} from './toggleBar'
import {Route} from './route'


export class SessionForm extends React.Component {
  state = {
    selectedSession: 'L',
    selectedGrade: '',
    selectedLetter: '',
    sessions: [
      {type: 'Top Rope', value: 'TR', isActive: false},
      {type: 'Lead', value: 'L', isActive: true},
      {type: 'Boulder', value: 'boulder', isActive: false},
    ],
    grades: [
      {grade: '6', value: '5.6', isActive: false},
      {grade: '7', value: '5.7', isActive: false},
      {grade: '8', value: '5.8', isActive: false},
      {grade: '9', value: '5.9', isActive: false},
      {grade: '10', value: '5.10', isActive: false},
      {grade: '11', value: '5.11', isActive: false},
      {grade: '12', value: '5.12', isActive: false},
      {grade: '13', value: '5.13', isActive: false},
      {grade: '14', value: '5.14', isActive: false}
    ],
    letters: [
      {grade: 'a', value: 'a', isActive: false},
      {grade: 'b', value: 'b', isActive: false},
      {grade: 'c', value: 'c', isActive: false},
      {grade: 'd', value: 'd', isActive: false},
      {grade: '+', value: '+', isActive: false},
      {grade: '-', value: '-', isActive: false},
    ],
    tracking: [
    ]
  }

  displayTracking() {
    if (this.state.tracking.length) {
      return (
        <ol class="list-group" reversed>
          {this.state.tracking.map((trackedRoute, index) =>
            <Route
              handleFalls={(e) => this.handleOptionChange(e, index, 'falls')}
              handleCompletion={(e) => this.handleOptionChange(e, index, 'completion')}
              {...trackedRoute}
            />)
          }
        </ol>
      )
    } else {
       return <h5 style={{textAlign: 'center', marginTop: '5%'}}>No Routes Added</h5>
    }
  }

  handleSessionChange(changeEvent, index) {
    this.setState({
      selectedSession: changeEvent.target.value,
      sessions: this.state.sessions.map((session, position) => {
        if (position === index) {
          session.isActive = true;
        } else {
          session.isActive = false;
        }
        return session
      })
    })
  }

  handleGradeChange(changeEvent, index) {
    const letterLessGrades = ['5.6', '5.7', '5.8', '5.9']
    if (letterLessGrades.includes(changeEvent.target.value)) {
      this.setState({
        selectedGrade: changeEvent.target.value,
        grades: this.state.grades.map((grade, position) => {
          if (position === index) {
            grade.isActive = true;
          } else {
            grade.isActive = false
          }
          return grade
        }),
        letters: this.state.letters.map(letter => {
          letter.isActive = false;
          return letter
        })
      }, () => this.setState({
        tracking: [
          {
            type: this.state.selectedSession,
            grade: this.state.selectedGrade,
            letter: '',
            completion: 'redpoint',
            falls: '0'
          },
          ...this.state.tracking
        ]
      }))
    } else {
      this.setState({
        selectedGrade: changeEvent.target.value,
        grades: this.state.grades.map((grade, position) => {
          if (position === index) {
            grade.isActive = true;
          } else {
            grade.isActive = false
          }
          return grade
        }),
        letters: this.state.letters.map(letter => {
          letter.isActive = false;
          return letter
        })
      })
    }
  }

  handleLetterChange(changeEvent, index) {
    const letterLessGrades = ['5.6', '5.7', '5.8', '5.9']
    if (letterLessGrades.includes(this.state.selectedGrade)) {
      return
    }
    this.setState({
      selectedLetter: changeEvent.target.value,
      letters: this.state.letters.map((letter, position) => {
        if (position === index) {
          letter.isActive = true;
        } else {
          letter.isActive = false
        }
        return letter
      })
    }, () => this.setState({
      tracking: [
        {
          type: this.state.selectedSession,
          grade: this.state.selectedGrade,
          letter: this.state.selectedLetter,
          completion: 'redpoint',
          falls: '0'
        },
        ...this.state.tracking,
      ]})
    )
  }

  handleOptionChange(changeEvent, index, property) {
    this.setState({
      tracking: this.state.tracking.map((trackedRoute, position) => {
        if (position == index) {
          trackedRoute[property] = changeEvent.target.value
        }
        return trackedRoute
      }),
      ...this.state.tracking
    })
  }

  handleSubmit = () => {
    let session;
    if (
      this.state.selectedSession === 'L' ||
      this.state.selectedSession === 'TR'
    ) {
      session = 'ropes'
    } else {
      session = 'bouldering'
    }
    const data = {
      session_type: session,
      routes: this.state.tracking
    }
    axios.post('/session', data).then(res => console.log(res))
    this.setState({
      tracking: []
    })
  }

  render() {
    return (
      <div class="container">
        <div class="session-form">
          <div class="session-selection">
            <div class="btn-group btn-group-toggle">
              {this.state.sessions.map((session, index) =>
                <ButtonInput
                  name='session-input'
                  grade={session.type}
                  isActive={session.isActive}
                  value={session.value}
                  handleClick={(e) => this.handleSessionChange(e, index)}
                />
              )}
            </div>
          </div>
          <div class="grade-input">
            <div class="numberInput-group">
              <div class="btn btn-primary disabled">5</div>
              {this.state.grades.map((grade, index) =>
                <ButtonInput
                  name="number-input"
                  handleClick={(e) => this.handleGradeChange(e, index)}
                  {...grade}/>
              )}
            </div>
            <div class="numberInput-group">
              {this.state.letters.map((letter, index) =>
                <ButtonInput
                  name="letter-input"
                  handleClick={(e) => this.handleLetterChange(e, index)}
                  {...letter} />
              )}
            </div>
          </div>
          <div class="session-tracking border rounded">
            {
              this.displayTracking()
            }
            <div class="submit">
              <button class="btn btn-primary" onClick={this.handleSubmit}>Submit</button>
            </div>
          </div>
        </div>
      </div>
    )
  }
}
