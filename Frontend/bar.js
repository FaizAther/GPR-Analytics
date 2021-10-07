import React from 'react';
import "./App.css";
 import {
    Chart,
    ChartTitle,
    ChartLegend,
    ChartSeries,
    ChartSeriesItem,
    ChartCategoryAxis,
    ChartCategoryAxisTitle,
    ChartCategoryAxisItem,
  } from "@progress/kendo-react-charts";
  import { COLORS } from "../../constants";
  
  // Graph data
  const series = [
    {
      status: "Total",
      data: [700, 700, 700, 700, 700, 700],
      color: COLORS.total,
    },
    {
      status: "Present",
      data: [288, 250, 274, 294, 282, 260],
      color: COLORS.present,
    },
    {
      status: "Absent",
      data: [12, 50, 26, 6, 18, 40],
      color: COLORS.absent,
    },
  ];
  
  const categories = ["Week1", "Week2", "Week3", "Week4", "Week5", "Week6"];
  
  const seriesLabels = {
    visible: true,
    padding: 3,
    font: "normal 16px Robotic, sans-serif",
    position: "center",
  };
  
  const Bar = props => { 
    return (
      <Chart>
        <ChartTitle text="Class Participation (Weekly)" />
        <ChartLegend visible={true} />
        <ChartCategoryAxis>
          <ChartCategoryAxisItem categories={categories}>
            <ChartCategoryAxisTitle text="Weeks" />
          </ChartCategoryAxisItem>
        </ChartCategoryAxis>
        <ChartSeries>
          {series.map((item, idx) => (
            <ChartSeriesItem
              key={idx}
              type="bar"
              gap={2}
              spacing={0.25}
              labels={seriesLabels}
              data={item.data}
              name={item.status}
              color={item.color}
            />
          ))}
        </ChartSeries>
      </Chart>
    );
  };

  
  export default Bar;