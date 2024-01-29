import React, { useState, useEffect } from 'react';
import {
    Box,
    Button,
    Grid,
    Typography,
    useTheme,
    IconButton,
} from '@mui/material';
import {
    CameraAlt as CameraAltIcon,
    Speed as SpeedIcon,
    ReportProblem as ReportProblemIcon,
    Autorenew as AutorenewIcon,
} from '@mui/icons-material';
import ChartCard from '../../components/ChartCard';
import Header from '../../components/Header';
import { ColorModeContext, tokens } from '../../theme';



const Thread = ({ title, Icon }) => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const [status, setStatus] = useState('Stopped');
    const [startTime, setStartTime] = useState(null);
    const [duration, setDuration] = useState('0s');

    useEffect(() => {
        let interval = null;
        if (status === 'Running') {
            interval = setInterval(() => {
                const now = Date.now();
                const timeDifference = now - startTime;
                const seconds = Math.floor((timeDifference / 1000) % 60);
                const minutes = Math.floor((timeDifference / (1000 * 60)) % 60);
                const hours = Math.floor((timeDifference / (1000 * 60 * 60)) % 24);
                setDuration(`${hours}h ${minutes}m ${seconds}s`);
            }, 1000);
        } else if (status === 'Stopped' && startTime !== null) {
            clearInterval(interval);
        }
        return () => clearInterval(interval);
    }, [status, startTime]);

    const handleButtonClick = () => {
        if (status === 'Stopped') {
            setStatus('Running');
            setStartTime(Date.now());
        } else {
            setStatus('Stopped');
            setStartTime(null);
        }
    };

    return (
        <Grid container spacing={3} marginLeft={20}>
            <Grid item xs={3}>
                <Box display="flex" alignItems="center">
                    <IconButton>{<Icon />}</IconButton>
                    <Typography variant="h5">{title}</Typography>
                </Box>
            </Grid>
            <Grid item xs={3}>
                <Button
                    variant="contained"
                    color={status === 'Stopped' ? 'primary' : 'secondary'}
                    onClick={handleButtonClick}

                >
                    {status === 'Stopped' ? 'Start' : 'Stop'}
                </Button>
            </Grid>
            <Grid item xs={3}>
                <Typography>{status}</Typography>
            </Grid>
            <Grid item xs={3}>
                <Typography>{duration}</Typography>
            </Grid>
        </Grid>
    );
};



const ServerStatus = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    return (
        <Box>
            <Box margin="20px">
                <Header title="SERVER STATUS" subtitle="" />
            </Box>

            <Box marginTop={3} />
            <ChartCard size={{ width: '100%', height: '300px' }} >

            </ChartCard>

            <Button
                variant="contained"
                style={{
                    margin: '2rem auto',
                    display: 'block',
                    backgroundColor: colors.whiteAccent[500],
                    color: colors.primary[400],
                    fontWeight: 'bold',


                }}
            >
                Start Server
            </Button>

            <Box
                display="flex"
                justifyContent="space-around"
                flexWrap="wrap"
                height={'500px'}
                style={{
                    margin: '200px',
                    border: '1px dotted',
                    borderRadius: '1%',
                    borderColor: colors.primary[400],

                }}

            >
                <Box>
                </Box>
                <Box
                    display="flex"
                    justifyContent="center"
                    alignItems="center"
                    mr={'30%'}



                >
                    <Typography variant="h3" style={{
                        fontWeight: 'bold',
                        marginTop: '2px'
                    }}>
                        Threads Status
                    </Typography>
                </Box>
                <Thread title="Camera Thread" Icon={CameraAltIcon} />
                <Thread title="ALPR Thread" Icon={AutorenewIcon} />
                <Thread title="Speed Thread" Icon={SpeedIcon} />
                <Thread title="Violation Thread" Icon={ReportProblemIcon} />
            </Box>
        </Box>
    );
};

export default ServerStatus;
