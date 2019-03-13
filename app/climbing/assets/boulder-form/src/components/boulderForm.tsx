import React from 'react';
import axios from 'axios';
import jwt from 'jsonwebtoken';
import moment from 'moment';

import {ButtonInput} from './toggleBar';
import {BoulderRoute, BoulderRouteProps} from './boulderRoute';

interface BoulderFormState {
  grades: string[];
  identity: number;
  tracking: any[];
}

export class BoulderForm extends React.Component<any, BoulderFormState> {
  state = {
    identity: 0,
    grades: [],
    tracking: []
  }

  componentDidMount() {
    this.setBoulderGrades()
    axios.post('/wctoken').then(res => {
      localStorage.setItem('token', res.data['access_token'])
      let {identity} = jwt.decode(res.data['access_token']) as any
      this.setState({
        identity: identity
      })
    })
  }

  setBoulderGrades() {
    let grades = ['VB']
    Array.from({length: 12}, (v, k) => grades.push(`V${k + 1}`))
    this.setState({
      grades: grades
    })
  }

  handleGradeClick(grade: string) {
    this.setState({
      tracking: [
        {
          type: 'bouldering',
          grade: grade,
          letter: '',
          timestamp: moment().utc(),
          completion: 'redpoint',
          falls: '0'
        },
        ...this.state.tracking
      ]
    })
  }

  handleOptionChange(changeEvent: React.FormEvent, index: number, property: string) {
    this.setState({
      tracking: this.state.tracking.map((trackedRoute: any, position: number) => {
        if (position == index) {
          trackedRoute[property] = (changeEvent.target as HTMLInputElement).value
        }
        return trackedRoute
      }),
    })
  }

  handleSubmit = () => {
    const data = {
      user: this.state.identity,
      type: 'bouldering',
      routes: this.state.tracking
    }
    let token = localStorage.getItem('token')
    axios.post('/api/session', data, {headers: {authorization: `Bearer ${token}`}}).then(res => console.log(res))
    this.setState({
      tracking: []
    })
  }

  displayTracking() {
    if (this.state.tracking.length) {
      return (
        <ol className="list-group">
          {this.state.tracking.map((trackedRoute, index) =>
            <BoulderRoute
            key={index}
            handleFalls={(e: React.FormEvent) => this.handleOptionChange(e, index, 'falls')}
            handleCompletion={(e: React.FormEvent) => this.handleOptionChange(e, index, 'completion')}
            {...trackedRoute}
            />
          )}
        </ol>
      )
    } else {
       return <h5 style={{textAlign: 'center', marginTop: '5%'}}>No Routes Added</h5>
    }
  }

  render() {
    return (
      <div className="container">
        <div className="bouldering-form">
          <div className="grade-input">
            {this.state.grades.map((grade, index) =>
              <ButtonInput
                key={index}
                grade={grade}
                handleClick={() => this.handleGradeClick(grade)}
              />
            )}
          </div>
          <div className="tracking border rounded">
            {this.displayTracking()}
            <div className="submit">
              <button className="btn btn-primary" onClick={this.handleSubmit}>Submit</button>
            </div>
          </div>
        </div>
      </div>
    )
  }
}
