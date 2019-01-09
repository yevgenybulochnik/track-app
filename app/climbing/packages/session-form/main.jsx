import React from 'react';
import ReactDOM from 'react-dom';

const GradeInput = ({grade, value}) =>
  <label class="btn btn-secondary">
    <input type="radio" value={value} /> {grade}
  </label>


class SessionForm extends React.Component {
  state = {
    grades: [
      {grade: '6', value: '5.6'},
      {grade: '7', value: '5.7'},
      {grade: '8', value: '5.8'},
      {grade: '9', value: '5.9'},
      {grade: '10', value: '5.10'},
      {grade: '11', value: '5.11'},
      {grade: '12', value: '5.12'},
      {grade: '13', value: '5.13'},
      {grade: '14', value: '5.14'}
    ],
    letters: [
      {grade: 'a', value: 'a'},
      {grade: 'b', value: 'b'},
      {grade: 'c', value: 'c'},
      {grade: 'd', value: 'd'},
      {grade: '+', value: '+'},
      {grade: '-', value: '-'},
    ]
  }

  render() {
    return (
      <div class="container">
        <div class="row">
          <div class="col-3 d-lg-none d-flex flex-column align-items-center">
            <div class="btn-group-vertical btn-group-toggle">
              <div class="btn btn-primary disabled">5</div>
              {this.state.grades.map(grade => <GradeInput {...grade} />)}
            </div>
            <div class="btn-group-vertical btn-group-toggle mt-3">
              {this.state.letters.map(letter => <GradeInput {...letter} />)}
            </div>
          </div>
          <div class="col-6 d-none d-lg-flex flex-column justify-content-start align-items-center">
            <div class="btn-group btn-group-toggle">
              <div class="btn btn-primary disabled">5</div>
              {this.state.grades.map(grade => <GradeInput {...grade} />)}
            </div>
            <div class="btn-group btn-group-toggle mt-3">
              {this.state.letters.map(letter => <GradeInput {...letter} />)}
            </div>
          </div>
          <div class="col-9 col-lg-6">
            test content
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
