import React, {Component} from 'react';
import {Pie} from 'react-chartjs-2';
import "./App.css";

class PieChartComponent extends Component {
    constructor(props){
        super(props)
        this.state= { labels: ['Present','Absent'],
        datasets: [{
            data:[260,40],
            backgroundColor: ['green','red']
            }]

        }
    }

  render(){

    return(
        <div className="avg">
            <p>
                <b><u>Total Class Participation for Current Week</u></b>
            </p>
        <Pie
          data={{
             labels: this.state.labels,
             datasets: this.state.datasets
          }}
          height='10%'
           />

        </div>
    );
  }
}  

 export default PieChartComponent;