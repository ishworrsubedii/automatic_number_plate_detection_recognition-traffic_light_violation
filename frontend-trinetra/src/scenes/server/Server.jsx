import React, { useState, useEffect } from 'react';
import {
    Box,
    Button,
    Grid,
    Typography,
    useTheme,
    IconButton,
} from '@mui/material';
import { Card, CardContent } from '@mui/material';

import {
    CameraAlt as CameraAltIcon,
    Autorenew as AutorenewIcon,
} from '@mui/icons-material';
import ChartCard from '../../components/ChartCard';
import Header from '../../components/Header';
import { tokens } from '../../theme';
import PinIcon from '@mui/icons-material/Pin';
import { useDispatch } from 'react-redux';
import { startCameraCapture, stopCameraCapture } from '../../actions/alpr/alprCaptureActions';
import { startImageLoad, stopImageLoad } from '../../actions/alpr/alprLoadActions';
import { startRecognition, stopRecognition } from '../../actions/alpr/alprRecognitionActions';
import TrafficIcon from '@mui/icons-material/Traffic';
import DirectionsCarIcon from '@mui/icons-material/DirectionsCar';
import SpeedIcon from '@mui/icons-material/Speed';

import { startCaptureTrafficlight, stopCaptureTrafficlight } from '../../actions/trafficlight/trafficlightCaptureActions';
import { startALPRTrafficLight, stopALPRTrafficLight } from '../../actions/trafficlight/trafficlightALPRActions';
import { startVehicleDetectionTrafficlight, stopVehicleDetectionTrafficlight } from '../../actions/trafficlight/trafficlightVehicleDetectionActions';
import { startTrafficlightNumberPlateDetection, stopTrafficlightNumberPlateDetection } from '../../actions/trafficlight/trafficlightNumberPlateDetectionActions';
import { startTrafficlightDetectionColor, stopTrafficlightDetectionColor } from '../../actions/trafficlight/trafficlightDetectionColorActions';

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
        else if (id === '11') {
            if (status === 'Stopped') {
                const newStartTime = Date.now();
                setStatus('Running');
                setStartTime(newStartTime);
                localStorage.setItem(`status-${id}`, 'Running');
                localStorage.setItem(`startTime-${id}`, newStartTime);
                dispatch(startCaptureTrafficlight());
            } else if (status === 'Running') {
                setStatus('Stopped');
                setStartTime(null);
                localStorage.setItem(`status-${id}`, 'Stopped');
                localStorage.removeItem(`startTime-${id}`);
                dispatch(stopCaptureTrafficlight());
            }
        }
        else if (id === '12') {
            if (status === 'Stopped') {
                const newStartTime = Date.now();
                setStatus('Running');
                setStartTime(newStartTime);
                localStorage.setItem(`status-${id}`, 'Running');
                localStorage.setItem(`startTime-${id}`, newStartTime);
                dispatch(startTrafficlightDetectionColor());
            } else if (status === 'Running') {
                setStatus('Stopped');
                setStartTime(null);
                localStorage.setItem(`status-${id}`, 'Stopped');
                localStorage.removeItem(`startTime-${id}`);
                dispatch(stopTrafficlightDetectionColor());
            }
        }
        else if (id === '13') {
            if (status === 'Stopped') {
                const newStartTime = Date.now();
                setStatus('Running');
                setStartTime(newStartTime);
                localStorage.setItem(`status-${id}`, 'Running');
                localStorage.setItem(`startTime-${id}`, newStartTime);
                dispatch(startVehicleDetectionTrafficlight());
            } else if (status === 'Running') {
                setStatus('Stopped');
                setStartTime(null);
                localStorage.setItem(`status-${id}`, 'Stopped');
                localStorage.removeItem(`startTime-${id}`);
                dispatch(stopVehicleDetectionTrafficlight());
            }
        }
        else if (id === '14') {
            if (status === 'Stopped') {
                const newStartTime = Date.now();
                setStatus('Running');
                setStartTime(newStartTime);
                localStorage.setItem(`status-${id}`, 'Running');
                localStorage.setItem(`startTime-${id}`, newStartTime);
                dispatch(startTrafficlightNumberPlateDetection());
            } else if (status === 'Running') {
                setStatus('Stopped');
                setStartTime(null);
                localStorage.setItem(`status-${id}`, 'Stopped');
                localStorage.removeItem(`startTime-${id}`);
                dispatch(stopTrafficlightNumberPlateDetection());
            }
        }
        else if (id === '15') {
            if (status === 'Stopped') {
                const newStartTime = Date.now();
                setStatus('Running');
                setStartTime(newStartTime);
                localStorage.setItem(`status-${id}`, 'Running');
                localStorage.setItem(`startTime-${id}`, newStartTime);
                dispatch(startALPRTrafficLight());
            } else if (status === 'Running') {
                setStatus('Stopped');
                setStartTime(null);
                localStorage.setItem(`status-${id}`, 'Stopped');
                localStorage.removeItem(`startTime-${id}`);
                dispatch(stopALPRTrafficLight());
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
    const rtspLinks = [
        { location: 'Baneshwor', link: 'rtsp://baneshwor' },
        { location: 'Koteshwor', link: 'rtsp://koteshwor' },
        { location: 'Kausaltar', link: 'rtsp://kausaltar' },
        { location: 'Teku', link: 'rtsp://teku' },
    ];

    return (
        <Box>
            <Box>
                <Box margin="20px">
                    <Header title="SERVER STATUS" subtitle="" />
                </Box>

                <Box marginTop={3} />
                <Typography variant="h7" style={{  marginLeft: '50%' }}>
                    RTSP Links
                </Typography>
                <ChartCard size={{ width: '100%', height: '300px' }}>
                
                    {rtspLinks.map((rtsp) => (
                        <Card key={rtsp.location} sx={{
                            width: '300px',
                            margin: '10px',
                            height: '100px',
                            backgroundColor: colors.primary[500],
                            color: colors.whiteAccent[100],
                            borderRadius: '10px',

                        }}>
                            <CardContent>
                                <Typography variant="h5" component="div">
                                    {rtsp.location}
                                </Typography>
                                <Typography variant="body2">
                                    {rtsp.link}
                                </Typography>
                            </CardContent>
                        </Card>
                    ))}
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



            <Box>
                <Box
                    display="flex"
                    justifyContent="space-around"
                    flexWrap="wrap"
                    height={'1000px'}
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
                            Traffic Light Violation Detection Thread
                        </Typography>
                    </Box>
                    <Thread id='11' title="Traffic Light Camera Thread" Icon={CameraAltIcon} />
                    <Thread id='12' title="Traffic Light And Color Detection" Icon={TrafficIcon} />
                    <Thread id='13' title="Vehicle Detection" Icon={DirectionsCarIcon} />
                    <Thread id='14' title="Vehicle Number Plate Detection" Icon={AutorenewIcon} />
                    <Thread id='15' title="ANPR" Icon={PinIcon} />
                </Box>
            </Box>
            <Box>
                <Box
                    display="flex"
                    justifyContent="space-around"
                    flexWrap="wrap"
                    height={'700px'}
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
                            Speed Estimation
                        </Typography>
                    </Box>
                    <Thread id='22' title="Speed Camera Thread" Icon={CameraAltIcon} />
                    <Thread id='22' title="Vehicle Speed Estimation" Icon={SpeedIcon} />
                    <Thread id='23' title="Vehicle Number Plate Detection" Icon={AutorenewIcon} />
                    <Thread id='24' title="ANPR" Icon={PinIcon} />
                </Box>
            </Box>
        </Box>

    );
};

export default ServerStatus;