import React from 'react';

export interface BoulderRouteProps {
  grade: string;
  completion: string;
  falls: string;
  handleFalls: () => void;
  handleCompletion: () => void;
}

export const BoulderRoute: React.SFC<BoulderRouteProps> = ({
  grade,
  completion,
  falls,
  handleFalls,
  handleCompletion,
}) =>
  <li className="list-group-item">
    <div className="route-info">
      <span style={{width: '4rem', textAlign: 'center'}}>{grade}</span>
      <div className="input-group-sm">
        <select className="custom-select" value={completion} onChange={handleCompletion}>
          <option value="redpoint">Redpoint</option>
          <option value="onsite">Onsite</option>
          <option value="project">Project</option>
        </select>
      </div>
      <div className="input-group-sm">
        <select className="custom-select" value={falls} onChange={handleFalls}>
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
