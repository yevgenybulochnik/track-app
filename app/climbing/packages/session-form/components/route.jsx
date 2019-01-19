import React from 'react'


export const Route = ({grade, letter, completion, falls, handleFalls, handleCompletion}) =>
  <li class="list-group-item">
    <div class="route-info">
      <span style={{width: '3rem'}}>{grade}{letter}</span>
      <div class="input-group-sm">
        <select class="custom-select" value={completion} onChange={handleCompletion}>
          <option value="redpoint">Redpoint</option>
          <option value="onsite">Onsite</option>
          <option value="project">Project</option>
        </select>
      </div>
      <div class="input-group-sm">
        <select class="custom-select" value={falls} onChange={handleFalls}>
          <option value="0">Falls</option>
          <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          <option value="6">6</option>
          <option value="7">7</option>
          <option value="8">8</option>
        </select>
      </div>
    </div>
  </li>
