import React from 'react';
import CourseName from './CourseName';
import Lecture from './lecture';
import Image from './image';
import PieChartComponent from './avg_participation';
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css"

function App() {
  return(
    
    <div id="title"><a href="Course Participation.html" class = "title_prop"> 
    SmartEd </a>
    
     <CourseName/>
     <Image/>
     <Lecture/>
     <PieChartComponent/>
      
       </div>
      
      
  );
}



export default App;