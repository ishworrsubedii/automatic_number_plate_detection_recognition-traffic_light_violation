import React, { useState } from "react";
import { Box, Button, useTheme, Grid, Card, CardActions, IconButton } from "@mui/material";
import LiveIcon from "@mui/icons-material/LiveTv"; // Import Live TV icon
import LibraryIcon from "@mui/icons-material/LibraryBooks"; // Import Library Books icon
import Header from "../../components/Header";
import ChartCard from "../../components/ChartCard";
import CameraInfo from "../../components/CameraInfo"
import { useMemo } from 'react';
import {
    MaterialReactTable,
    useMaterialReactTable,
} from 'material-react-table';
import { tokens } from "../../theme";
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { saveAs } from 'file-saver';
import ModalImage from 'react-modal-image';


import { fetchAlprDataTrafficLight } from "../../actions/trafficlight/trafficlightAutomaticNumberPlateRecognitionActions"
import { fetchRecognizedImagesPathTrafficLight, fetchNonRecognizedImagesPathTrafficLight } from "../../actions/trafficlight/trafficlightFetchAlprDataActions"
import { fetchDetectedImagesPathTrafficLight, fetchNonDetectedImagesPathTrafficLight } from "../../actions/trafficlight/trafficllightVehicleDetectedNonDetectedActions"
import DownloadIcon from '@mui/icons-material/Download';

const TrafficLightViolation = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);


    const [selectedTab, setSelectedTab] = useState("Live");
    const dispatch = useDispatch();
    const alprViolationData = useSelector((state) => state.fetchALPRResultTrafficLight.alprViolationData);

    useEffect(() => {
        dispatch(fetchAlprDataTrafficLight());
    }, [dispatch]);


    const columns = useMemo(
        () => [
            {
                accessorKey: 'id',
                header: 'ID',
                size: 100,
                sortable: false
            },

            {
                accessorKey: 'violation_id',
                header: 'Violation',
                size: 150,
                sortable: false
            },
            {
                accessorKey: 'image_path',
                header: 'Image Path',
                size: 50,
                sortable: false
            },
            {
                accessorKey: 'recognized_info',
                header: 'Recognized Info',
                size: 150,
                sortable: false
            },
            {
                accessorKey: 'accuracy',
                header: 'Accuracy',
                size: 100,
                sortable: false
            },
            {
                accessorKey: 'date',
                header: 'Violation Date',
                size: 150,
                sortable: false
            }, {
                accessorKey: 'violation_type',
                header: 'Violation Type',
                size: 150,
                sortable: false
            }, {
                accessorKey: 'status',
                header: 'Status',
                size: 150,
                sortable: false
            },
        ],
        []
    );
    const table = useMaterialReactTable({
        columns,
        data: alprViolationData,
    });

    const Live = () => {
        return (
            <Box>
                <ChartCard size={{ width: '100%', height: '300px' }}  >
                    <CameraInfo />
                </ChartCard>

                <Box width={'80%'}
                    margin={20}
                >
                    <MaterialReactTable table={table} />
                </Box>
            </Box>
        );
    };

    const VehicleDetectionLibrary = () => {
        const imgdetectededPaths = useSelector(state => state.imagePathDetectedNonDetTrafficLight.imgdetectededPaths);
        const imgnondetectededPaths = useSelector(state => state.imagePathDetectedNonDetTrafficLight.imgnondetectededPaths);
        const dispatch = useDispatch();
      


        useEffect(() => {
            dispatch(fetchDetectedImagesPathTrafficLight());
            dispatch(fetchNonDetectedImagesPathTrafficLight());
        }, [dispatch]);

        const [showDetected, setShowDetected] = useState(true);

        const imagesToShow = showDetected ? imgdetectededPaths : imgnondetectededPaths;

        const handleDownload = (image) => {
            saveAs(`http://127.0.0.1:8000/static/${image.traffic_light_violated_images || image.vehicle_not_detected_images}`, `Image_${image.id}.jpg`);
        };

        return (
            <div>
                <div>
                    <Button variant="contained" color="primary" onClick={() => setShowDetected(true)}>
                        Show Detected Images
                    </Button>
                    <Button variant="contained" color="secondary" onClick={() => setShowDetected(false)}>
                        Show Non-Detected Images
                    </Button>
                </div>
                <Box mt={5} />

                <Grid container spacing={2}>
                    {imagesToShow && imagesToShow.map((image) => (
                        <Grid item xs={12} sm={6} key={image.id}>
                            <Card style={{ padding: '20px', width: '800px', height: '300px' }}>
                                <ModalImage
                                    className="image"
                                    small={`http://127.0.0.1:8000/static/${image.traffic_light_violated_images || image.vehicle_not_detected_images}`}
                                    large={`http://127.0.0.1:8000/static/${image.traffic_light_violated_images || image.vehicle_not_detected_images}`}
                                    alt={`Image ${image.id}`}
                                    style={{ width: '100%', height: 'auto', objectFit: 'cover' }}
                                />
                                <CardActions>
                                    <IconButton onClick={() => handleDownload(image)}>
                                        <DownloadIcon />
                                    </IconButton>
                                </CardActions>
                            </Card>
                        </Grid>
                    ))}
                </Grid>
            </div>
        );

    };


    const RecognitionResultLibrary = () => {
        const recognizedPaths = useSelector(state => state.fetchRecognizedImagesPathTrafficLight.recognizedPaths);
        const nonRecognizedPaths = useSelector(state => state.fetchRecognizedImagesPathTrafficLight.nonRecognizedPaths);
        const dispatch = useDispatch();

        useEffect(() => {
            dispatch(fetchRecognizedImagesPathTrafficLight());
            dispatch(fetchNonRecognizedImagesPathTrafficLight());
        }, [dispatch]);

        const [showRecognized, setShowRecognized] = useState(true);

        const imagesToShow = showRecognized ? recognizedPaths : nonRecognizedPaths;

        const handleDownload = (image) => {
            saveAs(`http://127.0.0.1:8000/static/${image.recognized_image_path || image.non_recognized_image_path}`, `Image_${image.id}.jpg`);
        };

        return (
            <div>
                <div>
                    <Button variant="contained" color="primary" onClick={() => setShowRecognized(true)}>
                        Show Recognized Images
                    </Button>
                    <Button variant="contained" color="secondary" onClick={() => setShowRecognized(false)}>
                        Show Non-Recognized Images
                    </Button>
                </div>
                <Box mt={5} />

                <Grid container spacing={2}>
                    {imagesToShow && imagesToShow.map((image) => (
                        <Grid item xs={12} sm={6} key={image.id}>
                            <Card style={{ padding: '20px', width: '800px', height: '300px' }}>
                                <ModalImage
                                    className="image"
                                    small={`http://127.0.0.1:8000/static/${image.recognized_image_path || image.non_recognized_image_path}`}
                                    large={`http://127.0.0.1:8000/static/${image.recognized_image_path || image.non_recognized_image_path}`}
                                    alt={`Image ${image.id}`}
                                    style={{ width: '100%', height: 'auto', objectFit: 'cover' }}
                                />
                                <CardActions>
                                    <IconButton onClick={() => handleDownload(image)}>
                                        <DownloadIcon />
                                    </IconButton>
                                </CardActions>
                            </Card>
                        </Grid>
                    ))}
                </Grid>
            </div>
        );
    }

    const handleTabClick = (tab) => {
        setSelectedTab(tab);
    };



    return (
        <Box>
            <Box margin="20px">
                <Box
                    display="flex"
                    justifyContent="space-between"
                    alignContent="center"
                >
                    <Header title="TRAFFIC LIGHT VIOLATION" />
                </Box>
            </Box>
            <Box
                margin={5}
            >
                <Button
                    onClick={() => handleTabClick("Live")}
                    sx={{
                        borderBottom: selectedTab === "Live" && `2px solid ${colors.greenAccent[500]}`,
                        marginRight: 2,
                        color: colors.primary[200]
                    }}
                >
                    <LiveIcon sx={{ marginRight: 1, color: colors.primary[200] }} />
                    Live
                </Button>
                <Button
                    onClick={() => handleTabClick("Vehicle Detection Library")}
                    sx={{
                        borderBottom: selectedTab === "Vehicle Detection Library" && `2px solid ${colors.greenAccent[500]}`,
                        color: colors.primary[200]
                    }}
                >
                    <LibraryIcon sx={{ marginRight: 1, color: colors.primary[200] }} />
                    Vehicle Detection Library
                </Button>
                <Button
                    onClick={() => handleTabClick("Recognition Result Library")}
                    sx={{
                        borderBottom: selectedTab === "Recognition Result Library" && `2px solid ${colors.greenAccent[500]}`,
                        color: colors.primary[200]
                    }}
                >
                    <LibraryIcon sx={{ marginRight: 1, color: colors.primary[200] }} />
                    Recognition Result Library
                </Button>
            </Box>

            <Box mt={2}>
                {selectedTab === "Live" ?
                    <Live />
                    : selectedTab === "Vehicle Detection Library" ?
                        <VehicleDetectionLibrary />
                        : selectedTab === "Recognition Result Library" ?
                            <RecognitionResultLibrary />
                            : null
                }
            </Box>


        </Box>



    );
};

export default TrafficLightViolation;