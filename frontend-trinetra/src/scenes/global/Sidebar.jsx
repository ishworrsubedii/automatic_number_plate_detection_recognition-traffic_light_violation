import { useState } from "react";
import { ProSidebar as Sidebar, Menu, MenuItem } from "react-pro-sidebar";
import { Link } from "react-router-dom"; // for redirect
import { tokens } from "../../theme";
import { Box, Divider, IconButton, Typography, useTheme } from "@mui/material";
import "react-pro-sidebar/dist/css/styles.css";
import Button from "@mui/material/Button";

import DashboardIcon from "@mui/icons-material/Dashboard";
import { GrOverview } from "react-icons/gr";
import { BsCollection } from "react-icons/bs";

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

import GridViewRoundedIcon from "@mui/icons-material/GridViewRounded";
import ServerDnsOutlinedIcon from "@mui/icons-material/DnsOutlined";
import ConfirmationNumberIcon from "@mui/icons-material/ConfirmationNumber";
import SpeedIcon from "@mui/icons-material/Speed";
import TrafficIcon from "@mui/icons-material/Traffic";

import KeyboardArrowRightIcon from "@mui/icons-material/KeyboardArrowRight";
import KeyboardArrowUpIcon from "@mui/icons-material/KeyboardArrowUp";
import PeopleIcon from "@mui/icons-material/People";

import KeyboardArrowDownIcon from "@mui/icons-material/KeyboardArrowDown";
import ManageAccountsIcon from "@mui/icons-material/ManageAccounts";

import PieChartIcon from "@mui/icons-material/PieChart";
import AddchartIcon from "@mui/icons-material/Addchart";
import TimelineIcon from "@mui/icons-material/Timeline";

import profile from "../../assets/logo/profile.png";

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
  const [selected, setSelected] = useState("Dashboard");

  return (
    <Box
      sx={{
        "& .pro-sidebar-inner": {
          background: `${colors.primary[600]} !important`,
        },
        "& .pro-icon-wrapper": {
          backgroundColor: "transparent !important",
        },
        "& .pro-inner-item": {
          padding: "5px 35px 5px 20px !important",
        },
        "& .pro-inner-item:hover": {
          color: `${colors.primary[200]} !important`,
        },
        "& .pro-menu-item.active": {
          color: `${colors.greenAccent[600]} !important`,
        },
      }}
      height="213vh"
    >
      <Sidebar collapsed={isCollapsed}>
        <Menu iconShape="circle">
          <MenuItem
            onClick={() => setIsCollapsed(!isCollapsed)}
            icon={isCollapsed ? <MenuOutlinedIcon /> : undefined}
            style={{
              margin: "10px 0 30px 0",
              colors: colors.primary[200],
            }}
          >
            {!isCollapsed && (
              <Box>
                <Box
                  display="flex"
                  justifyContent="space-between"
                  alignItems="center"
                  ml="15px"
                >
                  <img
                    alt="profile-user"
                    width="30px"
                    height="30px"
                    src={profile} // path relative to the public directory
                    style={{
                      cursor: "pointer",
                      borderRadius: "50%",
                      marginRight: "10px",
                    }} // added marginRight
                  />
                  <Divider></Divider>
                  <Typography variant="h5" color={colors.greenAccent[500]}>
                    Ishwor Subedi
                  </Typography>

                  <IconButton style={{ marginLeft: "70px" }}>
                    <MenuOutlinedIcon />
                  </IconButton>
                </Box>
              </Box>
            )}
          </MenuItem>
          <Box paddingLeft={isCollapsed ? undefined : "10%"}>
            <Item
              title="Favorites"
              icon={<GridViewRoundedIcon />}
              to="/"
              selected={selected}
              setSelected={setSelected}
              style={{ fontWeight: "bold" }}
            />

            <Item
              title={"Overview"}
              icon={<GrOverview />}
              variant="h6"
              to="/overview"
              selected={selected}
              setSelected={setSelected}
            />

            <Item
              title={"Projects"}
              icon={<BsCollection />}
              to="/projects"
              selected={selected}
              setSelected={setSelected}
            />

            <Typography
              variant="h6"
              color={colors.primary[300]}
              sx={{ m: "15px 0 5px 20px" }}
            >
              Services
            </Typography>

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

            <Typography
              variant="h6"
              color={colors.primary[300]}
              sx={{ m: "15px 0 5px 20px" }}
            >
              Others
            </Typography>

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
                textDecorationColor: colors.greenAccent[500],
                borderRadius: "10px",
                height: "30px",
                width: "68px",
                padding: "10px",
                position: "absolute",
                top: "800px",
                left: "40%",
                transform: "translateX(-50%)",
                fontWeight: "bold",
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
