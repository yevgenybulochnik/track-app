import React from 'react'


export const ButtonInput = ({ name, grade, value, isActive, handleClick}) =>
  <label className={"btn btn-secondary " + (isActive ? "active" : "")}>
    <input type="radio" name={name} value={value} onClick={handleClick}/> {grade}
  </label>
