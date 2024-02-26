import React, { useState, useEffect, useMemo } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Box, Button, useTheme, Grid, Card, CardMedia, CardActions, IconButton } from "@mui/material";
import LiveIcon from "@mui/icons-material/LiveTv";
import LibraryIcon from "@mui/icons-material/LibraryBooks";
import DownloadIcon from '@mui/icons-material/Download';
import Header from "../../components/Header";
import ChartCard from "../../components/ChartCard";
import CameraInfo from "../../components/CameraInfo";
import { fetchAlprData } from "../../actions/alprActions";
import { fetchNonRecognizedImagesPath, fetchRecognizedImagesPath } from "../../actions/imagePathFetchActions";
import ReactPaginate from 'react-paginate';
import ImageGallery from 'react-image-gallery';
import { saveAs } from 'file-saver';
import ModalImage from 'react-modal-image';

import {
    MaterialReactTable,
    useMaterialReactTable,
} from "material-react-table";
import { tokens } from "../../theme";
const AlprService = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const dispatch = useDispatch();
    const alprData = useSelector((state) => state.alpr.alprData);
    console.log(alprData);

    useEffect(() => {
        dispatch(fetchAlprData());
    }, [dispatch]);

    const [selectedTab, setSelectedTab] = useState("Live");

    const columns = useMemo(
        () => [
            {
                accessorKey: "id",
                header: "ID",
                size: 50,
                sortable: false,
            },
            {
                accessorKey: "image_path",
                header: "Image Path",
                size: 100,
                sortable: false,
            },

            {
                accessorKey: "detection_id",
                header: "Detection ID",
                size: 100,
                sortable: false,
            },
            {
                accessorKey: "recognized_info",
                header: "Recognized Info",
                size: 200,
                sortable: false,
            },
            {
                accessorKey: "accuracy",
                header: "Accuracy",
                size: 100,
                sortable: false,
            },
            {
                accessorKey: "date",
                header: "Date",
                size: 200,
                sortable: false,
            },
            {
                accessorKey: "status",
                header: "Status",
                size: 100,
                sortable: false,
            },
        ],
        []
    );

    const table = useMaterialReactTable({
        columns,
        data: alprData,
    });

    const Live = () => (
        <Box>
            <ChartCard size={{ width: "100%", height: "300px" }}>
                <CameraInfo />
            </ChartCard>
            <Box width={"80%"} margin={20}>
                <MaterialReactTable table={table} />
            </Box>
        </Box>
    );

    const Library = () => {
        const recognizedPaths = useSelector(state => state.imagePathFetch.recognizedPaths);
        const nonRecognizedPaths = useSelector(state => state.imagePathFetch.nonRecognizedPaths);
        const dispatch = useDispatch();

        useEffect(() => {
            dispatch(fetchRecognizedImagesPath());
            dispatch(fetchNonRecognizedImagesPath());
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
                    {imagesToShow.map((image) => (
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
    };
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
                    <Header title="AUTOMATIC LICENSE PLATE RECOGNITION" />
                </Box>
            </Box>
            <Box margin={5}>
                <Button
                    onClick={() => handleTabClick("Live")}
                    sx={{
                        borderBottom:
                            selectedTab === "Live" && `2px solid ${colors.greenAccent[500]}`,
                        marginRight: 2,
                        color: colors.primary[200],
                    }}
                >
                    <LiveIcon sx={{ marginRight: 1, color: colors.primary[200] }} />
                    Live
                </Button>
                <Button
                    onClick={() => handleTabClick("Library")}
                    sx={{
                        borderBottom:
                            selectedTab === "Library" &&
                            `2px solid ${colors.greenAccent[500]}`,
                        color: colors.primary[200],
                    }}
                >
                    <LibraryIcon sx={{ marginRight: '10%', color: colors.primary[200] }} />
                    Library
                </Button>
            </Box>

            <Box mt={2}>{selectedTab === "Live" ? <Live /> : <Library />}</Box>
        </Box>
    );
};

export default AlprService;
