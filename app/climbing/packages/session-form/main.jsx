import React from 'react';
import ReactDOM from 'react-dom';
import './main.scss'

const ButtonInput = ({ name, grade, value, isActive, handleChange}) =>
  <label class={"btn btn-secondary " + (isActive ? "active" : "")}>
    <input type="radio" name={name} value={value} onChange={handleChange}/> {grade}
  </label>


class SessionForm extends React.Component {
  state = {
    selectedSession: '',
    selectedGrade: '',
    selectedLetter: '',
    sessions: [
      {type: 'Top Rope', value: 'top rope'},
      {type: 'Lead', value: 'lead'},
      {type: 'Boulder', value: 'boulder'},
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
    tracking: []
  }

  handleGradeChange(changeEvent, index) {
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

  handleLetterChange(changeEvent, index) {
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
    })
    console.log(this.state)
  }

  render() {
    const {tracking} = this.state
    return (
      <div class="container">
        <div class="session-form">
          <div class="session-selection">
            <div class="btn-group btn-group-toggle">
              {this.state.sessions.map(session => <ButtonInput grade={session.type} />)}
            </div>
          </div>
          <div class="grade-input">
            <div class="numberInput-group">
              <div class="btn btn-primary disabled">5</div>
              {this.state.grades.map((grade, index) =>
                <ButtonInput
                  name="number-input"
                  handleChange={(e) => this.handleGradeChange(e, index)}
                  {...grade}/>
              )}
            </div>
            <div class="numberInput-group">
              {this.state.letters.map((letter, index) =>
                <ButtonInput
                  name="letter-input"
                  handleChange={(e) => this.handleLetterChange(e, index)}
                  {...letter} />
              )}
            </div>
          </div>
          <div class="session-tracking">
            {
              tracking? (
                <h5>No Routes Added</h5>
              ): (
                <div>session tracking</div>
              )
            }
          </div>
        </div>
      </div>
    )
  }
}

ReactDOM.render(
  React.createElement(SessionForm, window.props),
  window.react_mount
)
