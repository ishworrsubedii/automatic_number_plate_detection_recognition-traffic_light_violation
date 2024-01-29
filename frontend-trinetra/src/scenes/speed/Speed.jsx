import {React,useState} from 'react';
import { Box, IconButton, useTheme, Divider,Typography,Button } from "@mui/material";
import { ColorModeContext, tokens } from "../../theme";
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


import speeddata from "../../data/main service data/speedDummiesData.json";

const SpeedTest = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const [selectedTab, setSelectedTab] = useState("Live");

    const columns = useMemo(
        () => [
            {
                accessorKey: 'violation_id',
                header: 'Violation ID',
            },
            {
                accessorKey: 'speed',
                header: 'Speed',
            },
            {
                accessorKey: 'recognized_info',
                header: 'Recognized Info',
            },
            {
                accessorKey: 'accuracy',
                header: 'Accuracy',
            },
            {
                accessorKey: 'date',
                header: 'Date',
            },
            {
                accessorKey: 'status',
                header: 'Status',
            },
        ],
        []
    );
    const table = useMaterialReactTable({
        columns,
        data: speeddata,
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

    const Library = () => {
        return (
            <Box>
                <Typography variant="h6">Library</Typography>
            </Box>

        )

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
                    <Header title="SPEED ESTIMATION" />
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
                    onClick={() => handleTabClick("Library")}
                    sx={{
                        borderBottom: selectedTab === "Library" && `2px solid ${colors.greenAccent[500]}`,
                        color: colors.primary[200]
                    }}
                >
                    <LibraryIcon sx={{ marginRight: 1, color: colors.primary[200] }} />
                    Library
                </Button>
            </Box>

            <Box mt={2}>
                {selectedTab === "Live" ? <Live /> : <Library />}
            </Box>


        </Box>



    );
};
export default SpeedTest;