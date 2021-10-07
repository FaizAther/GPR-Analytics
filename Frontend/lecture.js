import React from 'react';
import "./App.css";

function Lecture() {
    return(
        <div className="lec_info">
            <p>Number Of Lectures attended : <b>5</b>
            </p>
            <p>
                Number Of Lectures missed : <b>1</b>
            
            </p>
            <p>
                Total Number Of Students Enrolled In The Course : <b>300</b>
            </p>
        </div>
    );
}

export default Lecture;