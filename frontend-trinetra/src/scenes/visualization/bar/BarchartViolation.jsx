import React, { useEffect, useState } from 'react';
import ReactECharts from 'echarts-for-react';
import data from '../../../data/traffic_violations.json';
import { useTheme } from '@mui/material/styles';
import { tokens } from '../../../theme';


const BarchartTrafficRuleViolation = () => {
    const theme=useTheme();
    const colors = tokens(theme.palette.mode);
    const [option, setOption] = useState({});

    useEffect(() => {
        const groupedData = data.reduce((acc, item) => {
            if (!acc[item.violation_type]) {
                acc[item.violation_type] = [];
            }
            acc[item.violation_type].push(item.count);
            return acc;
        }, {});

        const series = Object.keys(groupedData).map(violation_type => ({
            name: violation_type,
            type: 'bar',
            data: groupedData[violation_type],
            lineStyle: {
                color: colors.primary[100]
            },
        }));

        setOption({
            tooltip: {},
            legend: {
                data: Object.keys(groupedData),
                bottom: 0,
                textStyle: {
                    color: colors.whiteAccent[100]
                }
                

            },
            grid: {
                left: '10%',
                right: '5%',
                bottom: '40%' // Increase this value to move the chart up
            },
            xAxis: {
                data: [...new Set(data.map(item => item.date))],
                axisLabel: {
                    rotate: 45,
                    interval: 0,
                }
            },
            yAxis: {},
            series,
            dataZoom: [
                {
                    startValue: data.length - 2,
                    endValue: data.length - 1,
                    type: 'slider',
                    bottom: 40
                },
                {
                    type: 'inside'
                }
            ]
        });
    }, []);

    return <ReactECharts option={option} style={{ height: '400px', width: '100%' }} />;
    
};

export default BarchartTrafficRuleViolation;