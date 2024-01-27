import React from 'react';
import { ResponsivePieCanvas } from '@nivo/pie';
import { useTheme } from '@mui/material/styles';
import { tokens } from '../../../theme';
const data = [
    { id: 'Koteshwor', value: 40 },
    { id: 'Balkumari', value: 38 },
    { id: 'Singhadurbar', value: 32 },
    { id: 'Jadibuti', value: 30 },
    { id: 'Teku', value: 28 },
    { id: 'Swayambhu', value: 26 },
    { id: 'Balaju', value: 22 },
    { id: 'Jorpati', value: 18 }
];

const PieCharts = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    return(
    <ResponsivePieCanvas
        data={data}
        margin={{ top: 40, right: 800, bottom: 40, left: 80 }}
        innerRadius={0.5}
        padAngle={0.7}
        cornerRadius={3}
        activeOuterRadiusOffset={8}
        colors={{ scheme: 'paired' }}
        borderColor={{
            from: 'color',
            modifiers: [
                [
                    'darker',
                    0.6
                ]
            ]
        }}
        arcLinkLabelsOffset={20}
        arcLinkLabelsSkipAngle={10}
        arcLinkLabelsTextColor={colors.primary[100]}
        arcLinkLabelsThickness={2}
        arcLinkLabelsColor={{ from: 'color' }}
        arcLabelsSkipAngle={10}
        arcLabelsTextColor={colors.whiteAccent[100]}
        defs={[
            {
                id: 'dots',
                type: 'patternDots',
                background: 'inherit',
                color: 'rgba(255, 255, 255, 0.3)',
                size: 4,
                padding: 1,
                stagger: true
            },
            {
                id: 'lines',
                type: 'patternLines',
                background: 'inherit',
                color: 'rgba(255, 255, 255, 0.3)',
                rotation: -45,
                lineWidth: 6,
                spacing: 10
            }
        ]}
        fill={[
            {
                match: {
                    id: 'ruby'
                },
                id: 'dots'
            },
            {
                match: {
                    id: 'c'
                },
                id: 'dots'
            },
            {
                match: {
                    id: 'go'
                },
                id: 'dots'
            },
            {
                match: {
                    id: 'python'
                },
                id: 'dots'
            },
            {
                match: {
                    id: 'scala'
                },
                id: 'lines'
            },
            {
                match: {
                    id: 'lisp'
                },
                id: 'lines'
            },
            {
                match: {
                    id: 'elixir'
                },
                id: 'lines'
            },
            {
                match: {
                    id: 'javascript'
                },
                id: 'lines'
            }
        ]}
        legends={[
            {
                anchor: 'right',
                direction: 'column',
                justify: false,
                translateX: 500,
                translateY: 0,
                itemsSpacing: 10,
                itemWidth: 60,
                itemHeight: 20,
                itemTextColor: colors.whiteAccent[100],
                itemDirection: 'left-to-right',
                itemOpacity: 1,
                symbolSize: 20,
                symbolShape: 'circle'
            }
        ]}
    />
    );
    };


export default PieCharts;