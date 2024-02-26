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
import PinIcon from '@mui/icons-material/Pin';
import { useDispatch } from 'react-redux';
import { startCameraCapture, stopCameraCapture } from '../../actions/alprCaptureActions';
import { startImageLoad, stopImageLoad } from '../../actions/alprLoadActions';
import { startRecognition, stopRecognition, fetchRecognitionStatus as fetchStatus } from '../../actions/alprRecognitionActions';

const Thread = ({ title, Icon, id }) => {
    const [status, setStatus] = useState('Stopped');
    const [startTime, setStartTime] = useState(null);
    const [duration, setDuration] = useState('0s');
    const dispatch = useDispatch();

    useEffect(() => {
        const savedStatus = localStorage.getItem(`status-${id}`);
        const savedStartTime = localStorage.getItem(`startTime-${id}`);
        if (savedStatus && savedStartTime) {
            setStatus(savedStatus);
            setStartTime(Number(savedStartTime));
        }

        dispatch(fetchStatus()).then((action) => {
            const { start_time, status } = action.payload;
            if (status === 'in_progress') {
                setStatus('Running');
                setStartTime(new Date(start_time));
            }
        });

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
        } else if (status !== 'Running' && startTime !== null) {
            clearInterval(interval);
        }
        return () => clearInterval(interval);
    }, [dispatch, id, status, startTime]);

    const handleButtonClick = () => {
        if (id === '1') {
            if (status === 'Stopped') {
                const newStartTime = Date.now();
                setStatus('Running');
                setStartTime(newStartTime);
                localStorage.setItem(`status-${id}`, 'Running');
                localStorage.setItem(`startTime-${id}`, newStartTime);
                dispatch(startCameraCapture());
            } else if (status === 'Running') {
                setStatus('Stopped');
                setStartTime(null);
                dispatch(stopCameraCapture());

                localStorage.setItem(`status-${id}`, 'Stopped');
                localStorage.removeItem(`startTime-${id}`);
            }
        } else if (id === '2') {
            if (status === 'Stopped') {
                const newStartTime = Date.now();
                setStatus('Running');
                setStartTime(newStartTime);
                localStorage.setItem(`status-${id}`, 'Running');
                localStorage.setItem(`startTime-${id}`, newStartTime);
                dispatch(startImageLoad());
            } else if (status === 'Running') {
                setStatus('Stopped');
                setStartTime(null);
                localStorage.setItem(`status-${id}`, 'Stopped');
                localStorage.removeItem(`startTime-${id}`);
                dispatch(stopImageLoad());
            }
        } else if (id === '3') {
            if (status === 'Stopped') {
                const newStartTime = Date.now();
                setStatus('Running');
                setStartTime(newStartTime);
                localStorage.setItem(`status-${id}`, 'Running');
                localStorage.setItem(`startTime-${id}`, newStartTime);
                dispatch(startRecognition());
            } else if (status === 'Running') {
                setStatus('Stopped');
                setStartTime(null);
                localStorage.setItem(`status-${id}`, 'Stopped');
                localStorage.removeItem(`startTime-${id}`);
                dispatch(stopRecognition());
            }
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
            <ChartCard size={{ width: '100%', height: '300px' }} />

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
                <Box></Box>
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
                        ALPR THREAD STATUS
                    </Typography>
                </Box>
                <Thread id='1' title="Camera Thread" Icon={CameraAltIcon} />
                <Thread id='2' title="Number Plate Detection Thread" Icon={AutorenewIcon} />
                <Thread id='3' title="ALPR Thread" Icon={PinIcon} />
            </Box>
        </Box>
    );
};

export default ServerStatus;