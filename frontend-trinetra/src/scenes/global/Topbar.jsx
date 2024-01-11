import { Box, IconButton, useTheme, Divider } from "@mui/material";
import { useContext } from "react";
import { ColorModeContext, tokens } from "../../theme";
import InputBase from "@mui/material/InputBase";
import LightModeOutlinedIcon from "@mui/icons-material/LightModeOutlined";
import DarkModeOutlinedIcon from "@mui/icons-material/DarkModeOutlined";
import NotificationsOutlinedIcon from "@mui/icons-material/NotificationsOutlined";
import SettingsOutlinedIcon from "@mui/icons-material/SettingsOutlined";
import PersonOutlinedIcon from "@mui/icons-material/PersonOutlined";
import SearchIcon from "@mui/icons-material/Search";
import Calendar from "@mui/icons-material/CalendarMonthTwoTone";
import Star from "@mui/icons-material/Star";

const Topbar = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const colorMode = useContext(ColorModeContext);

  return (
    <Box display="flex" justifyContent="space-between" p={2}>
      <Box>
      <IconButton type="button" sx={{ ml: "0px", flex: 0 }}>
            <Calendar />
            </IconButton>
            <IconButton type="button" sx={{ ml: "0px", flex: 0 }}>
            <Star />
            </IconButton>
      </Box>
      

      <Box display="flex">
        <Box display="flex"
          backgroundColor={
            theme.palette.mode === "dark" ? (
              colors.primary[400]
            ) :
              (
                colors.whiteAccent[420]

              )}
          borderRadius="3px"
          boxShadow="1"
        >
         

          <IconButton type="button" sx={{ p: 1 }}>
            <SearchIcon />
          </IconButton>
          <InputBase sx={{ mt: 2, ml: 1, flex: 1, height: 3, width: 200 }} placeholder="Search" />

        </Box>
        
        <IconButton onClick={colorMode.toggleColorMode}>
          {theme.palette.mode === "dark" ? (
            <DarkModeOutlinedIcon />
          ) : (
            <LightModeOutlinedIcon />
          )}
        </IconButton>
        <IconButton>
          <SettingsOutlinedIcon />
        </IconButton>
        <IconButton>
          <NotificationsOutlinedIcon />
        </IconButton>

        <IconButton>
          <PersonOutlinedIcon />
        </IconButton>

      </Box>

    </Box>

  );
};

export default Topbar;