import { useState } from "react";
import { Sidebar, Menu, MenuItem, SubMenu } from 'react-pro-sidebar';
import { Link } from "react-router-dom" // for redirect
import { tokens } from "../../theme";
import { Box, IconButton, useTheme, Divider } from "@mui/material";


import GridViewRoundedIcon from '@mui/icons-material/GridViewRounded';
import ServerDnsOutlinedIcon from '@mui/icons-material/DnsOutlined';
import ConfirmationNumberIcon from '@mui/icons-material/ConfirmationNumber';
import SpeedIcon from '@mui/icons-material/Speed';
import TrafficIcon from '@mui/icons-material/Traffic';


import KeyboardArrowRightIcon from '@mui/icons-material/KeyboardArrowRight';
import KeyboardArrowUpIcon from '@mui/icons-material/KeyboardArrowUp';
import PeopleIcon from '@mui/icons-material/People';

import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import ManageAccountsIcon from '@mui/icons-material/ManageAccounts';

import PieChartIcon from '@mui/icons-material/PieChart';
import AddchartIcon from '@mui/icons-material/Addchart';
import TimelineIcon from '@mui/icons-material/Timeline';


const CustomSidebar = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const [isCollapsed, setIsSelected] = useState(false);
    const [selected, setSelected] = useState("Dashboard")
    return (
        <Box>Sidebar

        </Box>)
}
export default CustomSidebar;