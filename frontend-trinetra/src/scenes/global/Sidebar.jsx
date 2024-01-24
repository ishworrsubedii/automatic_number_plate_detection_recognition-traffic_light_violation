import { useState } from "react";
import { ProSidebar as Sidebar, Menu, MenuItem } from 'react-pro-sidebar';
import { Link } from "react-router-dom" // for redirect
import { tokens } from "../../theme";
import { Box, Divider, IconButton, Typography, useTheme } from "@mui/material";
import "react-pro-sidebar/dist/css/styles.css";
import Button from '@mui/material/Button';

import PeopleOutlinedIcon from "@mui/icons-material/PeopleOutlined";
import ContactsOutlinedIcon from "@mui/icons-material/ContactsOutlined";
import ReceiptOutlinedIcon from "@mui/icons-material/ReceiptOutlined";
import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";
import CalendarTodayOutlinedIcon from "@mui/icons-material/CalendarTodayOutlined";
import HelpOutlineOutlinedIcon from "@mui/icons-material/HelpOutlineOutlined";
import BarChartOutlinedIcon from "@mui/icons-material/BarChartOutlined";
import PieChartOutlineOutlinedIcon from "@mui/icons-material/PieChartOutlineOutlined";
import TimelineOutlinedIcon from "@mui/icons-material/TimelineOutlined";
import MenuOutlinedIcon from "@mui/icons-material/MenuOutlined";
import MapOutlinedIcon from "@mui/icons-material/MapOutlined";


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


const Item = ({ title, to, icon, selected, setSelected }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  return (
    <MenuItem
      active={selected === title}
      style={{
        color: colors.primary[100],
      }}
      onClick={() => setSelected(title)}
      icon={icon}
    >
      <Typography>{title}</Typography>
      <Link to={to} />
    </MenuItem>
  );
};

const CustomSidebar = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const [isCollapsed, setIsCollapsed] = useState(false); // Add this line
  const [selected, setSelected] = useState("Dashboard")

  return (
    <Box
      sx={{
        "&.pro-sidebar-inner": {
          background: `${colors.primary[400]} !important`,
        },
        "&.pro-icon-wrapper": {
          backgroundColor: "transparent !important",
        },
        "&.pro-inner-item": {
          padding: "5px 35px 5px 20px !important",
        },
        "&.pro-inner-item:hover": {
          color: `${colors.whiteAccent} !important`,
        },
        "&.pro-menu-item.active": {
          color: "#6870fa !important",
        },
      }}
      backgroundColor={
        theme.palette.mode === "dark" ? (
          colors.primary[400]
        ) :
          (
            colors.whiteAccent[420]

          )}
    >
      <Sidebar collapsed={isCollapsed}

      >
        <Menu iconShape="circle">
          <MenuItem
            onClick={() => setIsCollapsed(!isCollapsed)}
            icon={isCollapsed ? < MenuOutlinedIcon /> : undefined}
            style={{
              margin: "10px 0 20px 0",
              colors: "#000000",
            }}
          >
            {!isCollapsed && (
              <Box>
                <Box display="flex" justifyContent="start" alignItems="center">
                  <img
                    alt="profile-user"
                    width="30px"
                    height="30px"
                    color="#000000"
                    src={"/logo/profile.png"} // path relative to the public directory
                    style={{ cursor: "pointer", borderRadius: "50%", marginRight: "10px" }} // added marginRight
                  />
                  <Divider>

                  </Divider>
                  <Typography>
                    Ishwor Subedi
                  </Typography>

                  <IconButton style={{ marginLeft: "70px" }}>
                    <MenuOutlinedIcon />
                  </IconButton>
                </Box>



              </Box>

            )
            }
          </MenuItem>
          <Box paddingLeft={isCollapsed ? undefined : "10%"}>
            <Item
              title="Favorites"
              to="/"
              selected={selected}
              setSelected={setSelected}
              style={{ fontWeight: "bold" }}
            />

            <Item
              title={ "Overview"}
              to="/overview"
              selected={selected}
              setSelected={setSelected}
            />

            <Item
              title={"Projects"}
              to="/projects"
              selected={selected}
              setSelected={setSelected}
            />

            <Item
              title="Dashboards"
              to="/"
              selected={selected}
              setSelected={setSelected}

            />

            <Item
              title="Default"
              to="/default"
              icon={<GridViewRoundedIcon />}
              selected={selected}
              setSelected={setSelected}
            />
            <Item
              title="Server"
              to="/server"
              icon={<ServerDnsOutlinedIcon />}
              selected={selected}
              setSelected={setSelected}
            />
            <Item
              title="ALPR"
              to="/alpr"
              icon={<ConfirmationNumberIcon />}
              selected={selected}
              setSelected={setSelected}
            />
            <Item
              title="Speed"
              to="/speedtest"
              icon={<SpeedIcon />}
              selected={selected}
              setSelected={setSelected}
            />
            <Item
              title="Violation"
              to="/violation"
              icon={<TrafficIcon />}
              selected={selected}
              setSelected={setSelected}
            />


            <Item
              title="Others"
              to="/"
              selected={selected}
              setSelected={setSelected}

            />

            <Item
              title="User Profile"
              to="/userprofile"
              icon={<PersonOutlinedIcon />}
              selected={selected}
              setSelected={setSelected}
            />
            <Item
              title="Account"
              to="/account"
              icon={<ContactsOutlinedIcon />}
              selected={selected}
              setSelected={setSelected}
            />
            <Item
              title="Corporate"
              to="/corporate"
              icon={<PeopleIcon />}
              selected={selected}
              setSelected={setSelected}
            />
            <Item
              title="Blog"
              to="/blog"
              icon={<ReceiptOutlinedIcon />}
              selected={selected}
              setSelected={setSelected}
            />
            <Item
              title="Camera List"
              to="/cameralist"
              icon={<MapOutlinedIcon />}
              selected={selected}
              setSelected={setSelected}
            />

            <Button
              style={{
                backgroundColor: colors.greenAccent[500],
                borderRadius: "10px",
                height: "40px",
                width: "100px",
                padding: "10px",
                position: "absolute",
                top: "89%",
                left: "40%",
                transform: "translateX(-50%)",
                fontWeight: "bold" // added fontWeight
              }}
            >
              Log Out
            </Button>
          </Box>






        </Menu>
      </Sidebar>

    </Box>
  );
};

export default CustomSidebar;