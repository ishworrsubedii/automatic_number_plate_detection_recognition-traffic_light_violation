import React, { useEffect } from 'react';
import * as echarts from 'echarts';
import { useTheme } from '@mui/material/styles';
import { tokens } from '../../../theme';

const BarChart = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    useEffect(() => {
        var chartDom = document.getElementById('main');
        var myChart = echarts.init(chartDom);
        var option;

        var series = [
            {
                data: [20, 25, 22, 27, 24, 23, 26],
                type: 'bar',
                stack: '2 Wheeler',
                name: '2 Wheeler',
                itemStyle: {
                    color: "#95A4FC", 
                    borderRadius: [20, 20, 0, 0]
                  }
            },
            {
                data: [30, 35, 32, 37, 34, 33, 36],
                type: 'bar',
                stack: '4 Wheeler',
                name: '4 Wheeler',
                itemStyle: {
                    color: colors.yellowAccent[500], 
                    borderRadius: [20, 20, 0, 0]
                  }
            },
            {
                data: [10, 15, 12, 17, 14, 13, 16],
                type: 'bar',
                stack: 'Heavy Vehicle',
                name: 'Heavy Vehicle',
                itemStyle: {
                    color: colors.blueAccent[500], 
                    borderRadius: [20, 20, 0, 0]
                  }
            }
        ];

        

        

        option = {
            xAxis: {
                type: 'category',
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            },
            yAxis: {
                type: 'value'
            },
            legend: {
                data: ['2 Wheeler', '4 Wheeler', 'Heavy Vehicle'],
                orient: 'horizontal',
                bottom: 0, 
                textStyle: {
                    
                    color: colors.primary[100]
                }
            },
            series: series
        };

        option && myChart.setOption(option);
    }, []);

    return (
        <div id="main" style={{  margin: '50px', display:'flex', flexDirection:'column', alignItems:'center', width: '100%', height: '375px' }} />
    );
};

export default BarChart;