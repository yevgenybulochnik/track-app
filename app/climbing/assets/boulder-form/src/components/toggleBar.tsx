import React from 'react';

interface BoulderGradeInput {
  key: number;
  grade: string;
  handleClick: () => void;
}

export const ButtonInput: React.SFC<BoulderGradeInput> = ({
  grade,
  handleClick
}) => 
  <button className="btn btn-secondary" onClick={handleClick}>{grade}</button>
