import React from 'react';
import { Box, Card, CardContent, Typography } from '@mui/material';

import { tokens } from '../theme';
import { useTheme } from '@mui/material/styles';

const ChartCard = ({ title, children,subtitle, size }) => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    return(
    <Card sx={{ borderRadius: 4, margin: '0 auto', maxWidth: '90%' }}>
        <CardContent>

            <Typography variant="h4" color={colors.primary[100]} align="center">{title} </Typography>
            <Typography variant="h6" color={colors.primary[200]} align="center">{subtitle}</Typography>



            <Box 
                width={size.width} 
                height={size.height} 
                display="flex" 
                justifyContent="center"
            >
                {children}
            </Box>
        </CardContent>
    </Card>
    );
    };

export default ChartCard;