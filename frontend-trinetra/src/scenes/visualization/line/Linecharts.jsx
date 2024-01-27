import React from 'react';
import ReactECharts from 'echarts-for-react';
import data from '../../../data/speedData.json';
import { useTheme } from '@mui/material/styles';
import { tokens } from '../../../theme';

const LineChart = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const option = {
       

        
        tooltip: {
            trigger: 'axis'
        },
        grid: {
            left: '10%',
            right: '10%',
            bottom: '45%' // Increase this value to move the chart up
        },
        xAxis: {
            type: 'category',
            data: data.map(item => item[0]),
            axisLabel: {
                rotate: 45,
                interval: 0
            }
        },
        yAxis: {},
        toolbox: {
            right: 10,
            feature: {
                dataZoom: {
                    yAxisIndex: 'none'
                },
                restore: {},
               
            }
        },
        dataZoom: [
            {
                startValue: data.length - 20,
                endValue: data.length -1,
                bottom: 40, 
                type: 'slider'
            },
            {
                type: 'inside'
            }
        ],
        visualMap: {
            bottom:0,
            right: 'center',
            orient: 'horizontal',
            textStyle: {
                color: colors.whiteAccent[100]
            },
            pieces: [
                { gt: 0, lte: 50, color: colors.blueAccent[500] },
                { gt: 50, lte: 100, color: colors.whiteAccent[100]},
                { gt: 100, lte: 150, color: colors.greenAccent[500] },
                { gt: 150, lte: 200, color: colors.primary[200] },
                { gt: 200, lte: 300, color: colors.yellowAccent[700] },
                { gt: 300, color: '#AC3B2A' }
            ],
            outOfRange: {
                color: colors.whiteAccent[400]
            }
        },
        
        series: {
            name: 'Average Speed',
            type: 'line',
            smooth: true, // Smooth the line
            showSymbol: false,
            data: data.map(item => item[1]),
            markLine: {
                silent: true,
                lineStyle: {
                    color: colors.primary[100]
                },
                data: [
                    { yAxis: 50 },
                    { yAxis: 100 },
                    { yAxis: 150 },
                    { yAxis: 200 },
                    { yAxis: 300 }
                ]
            },
            itemStyle: {
                color: '#ff6347' // Use a custom color for the line
            }
        },
    };

    return <ReactECharts option={option} style={{ height: '400px', width: '100%' }} />;
};

export default LineChart;