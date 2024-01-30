import React from "react";
import {
  Box,
  Paper,
  Typography,
  TextField,
  Button,
  useTheme,
  Grid,
  Checkbox,
  Link,
} from "@mui/material";
import { tokens } from "../../../theme";
import { Routes, Route, Navigate, useNavigate } from "react-router-dom";

import FormControlLabel from "@mui/material/FormControlLabel";

import InputAdornment from "@mui/material/InputAdornment";
import AccountCircle from "@mui/icons-material/AccountCircle";
import VpnKeyIcon from "@mui/icons-material/VpnKey";
import { BsGoogle } from "react-icons/bs";
import AppleIcon from "@mui/icons-material/Apple";
import SignUpPage from "../signup/Signup";
import trinetralogo from "../../../assets/trinetra.svg";

const LoginPage = ({ onLogin }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const handleLogin = (event) => {
    event.preventDefault();
    onLogin();
  };

  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "left",
        height: "100vh",
        width: "1000px",
      }}
    >
      <img
        src={trinetralogo}
        alt="Logo"
        style={{
          position: "absolute",
          top: 20,
          left: 20,
          width: "80px",
          height: "80px",
        }}
      />

      <Paper
        elevation={3}
        sx={{
          padding: "40px",
          width: "800px",
        }}
      >
        <Typography
          variant="h1"
          style={{ fontWeight: "bold" }}
          textAlign={"left"}
          marginTop={"100px"}
          marginLeft={"60px"}
          // margin={'100px'}
        >
          Let us be protected by the
          <div style={{ color: colors.greenAccent[500] }}>third eye!</div>
          <Typography
            variant="h5"
            margin={"20px"}
            fontStyle={"inherit"}
            color={colors.primary[100]}
          >
            Log in to trinetra to see the magic.
          </Typography>
        </Typography>

        <form onSubmit={handleLogin}>
          <form onSubmit={handleLogin}>
            <TextField
              label="Username"
              type="text"
              variant="outlined"
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <AccountCircle
                      style={{ fontSize: 20, color: colors.primary[100] }}
                    />
                  </InputAdornment>
                ),
              }}
              style={{
                borderRadius: 50,
                width: "80%",
                marginTop: "20px",
                marginLeft: "60px",
              }}
            />
            <TextField
              label="Password"
              type="password"
              variant="outlined"
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <VpnKeyIcon
                      style={{ fontSize: 20, color: colors.primary[100] }}
                    />
                  </InputAdornment>
                ),
              }}
              style={{
                borderRadius: 50,
                width: "80%",
                marginTop: "20px",
                marginLeft: "60px",
              }}
            />
          </form>
          <Grid
            container
            justifyContent="left"
            style={{ marginTop: "1%", marginLeft: "70px" }}
          >
            <FormControlLabel
              control={<Checkbox style={{ color: colors.greenAccent[500] }} />}
              label="Remember Password"
            />
            <Typography
              variant="h6"
              style={{
                cursor: "pointer",
                color: colors.greenAccent[500],
                marginLeft: "40%",
                marginTop: "1%",
              }}
            >
              Forgot Password?
            </Typography>
          </Grid>
          <Button
            type="submit"
            variant="contained"
            color="primary"
            style={{
              backgroundColor: colors.greenAccent[500],
              color: colors.primary[500],
              marginTop: "5%",
              marginLeft: "20%",
              height: "5%",
              width: "50%",
              fontSize: "18px",
            }}
          >
            <Typography style={{ fontWeight: "bold" }}>Login</Typography>
          </Button>

          <Box
            display="flex"
            alignItems="center"
            width="80%"
            margin="30px auto"
          >
            <Box
              flexGrow={1}
              borderBottom={1}
              borderColor={colors.primary[200]}
            />
            <Typography variant="h6" color="textSecondary" mx={2}>
              or continue with
            </Typography>
            <Box flexGrow={1} borderBottom={1} borderColor="grey.500" />
          </Box>
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              width: "80%",
              height: "10%",
              margin: "auto",
            }}
          >
            <Button
              variant="contained"
              style={{ marginTop: "20px", height: "60%" }}
            >
              <BsGoogle />
              <Box width={10} />
              Continue with Google
            </Button>
            <Box width={"30px"}></Box>

            <Button
              variant="contained"
              style={{ marginTop: "20px", height: "60%" }}
            >
              <AppleIcon />
              <Box width={10} />
              Continue with Apple
            </Button>
          </Box>
          <Box mt={"10%"} mb={2}>
            <Typography variant="body1">Don't have an account?</Typography>
            <Button component={Link} to="/signup" style={{ color: "#39FF14" }}>
              Sign up now
            </Button>
          </Box>
        </form>
      </Paper>
    </Box>
  );
};

export default LoginPage;
