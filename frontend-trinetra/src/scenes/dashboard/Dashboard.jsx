import { Box, IconButton, useTheme, Divider } from "@mui/material";
import { useContext } from "react";
import { ColorModeContext, tokens } from "../../theme";
import Header from '../../components/Header.jsx';import LightModeOutlinedIcon from "@mui/icons-material/LightModeOutlined";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import NotificationsOutlinedIcon from "@mui/icons-material/NotificationsOutlined";
import SettingsOutlinedIcon from "@mui/icons-material/SettingsOutlined";
import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";
import SearchIcon from "@mui/icons-material/Search";
const Dashboard = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    return (
        <Box margin="20px">
            <Box display="flex" justifyContent={"space-between"}alignContent={"center"}>

            <Header title="DASHBOARD" subtitle="Welcome to your dashboard">

                </Header>
            </Box>
        </Box>
    );
}
export default Dashboard;