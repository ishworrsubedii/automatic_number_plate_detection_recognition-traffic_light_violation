import React from "react";
import {
    Box,
    Card,
    useTheme,
    IconButton,
    Divider,
    Typography,
} from "@mui/material";
import Header from "../../components/Header.jsx";

import { tokens } from "../../theme";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";

const DashboardCard = ({ title, value, percentage, icon, customcolor }) => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    return (
        <Card
            sx={{
                flex: "200px",
                height: "70px",
                margin: "50px",
                bgcolor: customcolor,
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
                fontSize: "20px",
                borderRadius: "40px",
            }}
        >
            <Typography variant="h4" component="div" style={{ color: 'black' }}>
                {title}
            </Typography>
            <Box
                display="flex"
                justifyContent="center"
                alignItems="center"
                sx={{ width: "100%", mt: 1 }}
            >
                <Typography variant="h6" component="div" style={{ color: 'black' }}>
                    {value}
                </Typography>
                <Box display="flex" alignItems="center" sx={{ ml: 1 }}>
                    <Typography variant="h6" component="div" style={{ color: 'black' }}>
                        {percentage}
                    </Typography>
                </Box>
                <Box left={"30px"}>{icon}</Box>
            </Box>
        </Card>
    );
};

const Dashboard = () => {
    return (
        <Box>
            <Box margin="20px">
                <Box
                    display="flex"
                    justifyContent={"space-between"}
                    alignContent={"center"}
                >
                    <Header
                        title="DASHBOARD"
                        subtitle="Welcome to your dashboard"
                    ></Header>
                </Box>
            </Box>
            <Box
                display={"flex"}
                flexDirection={"row"}
                flexWrap="wrap"
                justifyContent="space-around"
            >
                <DashboardCard
                    title="Total Vehicles Detected"
                    value="721k"
                    percentage="+11.01%"
                    icon={<TrendingUpIcon style={{ color: 'black' }} />}
                    customcolor={"#E3F5FF"}

                />
                <DashboardCard
                    title="Number Plate Recognized"
                    value="367k"
                    percentage="-0.01%"
                    icon={<TrendingDownIcon style={{ color: 'black' }} />}
                    customcolor={"#E5ECF6"}

                />
                <DashboardCard
                    title="Over Speed"
                    value="1,156"
                    percentage="+15.03%"
                    icon={<TrendingUpIcon style={{ color: 'black' }} />}
                    customcolor={"#E3F5FF"}

                />
                <DashboardCard
                    title="Total Vehicles Detected"
                    value="239k"
                    percentage="+6.08%"
                    icon={<TrendingUpIcon style={{ color: 'black' }} />}
                    customcolor={"#E5ECF6"}

                />
            </Box>
        </Box>
    );
};

export default Dashboard;
