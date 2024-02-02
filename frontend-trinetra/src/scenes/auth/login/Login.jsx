import React, { useState, useEffect } from "react";
import {
  Box,
  Paper,
  Typography,
  TextField,
  Button,
  useTheme,
  Grid,
  Checkbox,
} from "@mui/material";

import { tokens } from "../../../theme";
import FormControlLabel from "@mui/material/FormControlLabel";
import InputAdornment from "@mui/material/InputAdornment";
import AccountCircle from "@mui/icons-material/AccountCircle";
import VpnKeyIcon from "@mui/icons-material/VpnKey";
import { BsGoogle } from "react-icons/bs";
import AppleIcon from "@mui/icons-material/Apple";
import trinetralogo from "../../../assets/trinetra.svg";

import { Link, useNavigate } from "react-router-dom";
import { connect } from "react-redux";
import { login } from "../../../actions/auth";
import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";

const LoginPage = ({ login, isAuthenticated }) => {
  const theme = useTheme();
  const navigate = useNavigate();
  const colors = tokens(theme.palette.mode);
  const [loading, setLoading] = useState(false);

  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarSeverity, setSnackbarSeverity] = useState("success");
  const [snackbarMessage, setSnackbarMessage] = useState("");
  const handleSnackbarOpen = (severity, message) => {
    setSnackbarSeverity(severity);
    setSnackbarMessage(message);
    setSnackbarOpen(true);
  };

  const handleSnackbarClose = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }
    setSnackbarOpen(false);
  };

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const { email, password } = formData;

  const onChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = async (e) => {
    e.preventDefault();
    try {
      const loginResult = await login(email, password);

      if (loginResult === "success") {
        handleSnackbarOpen("success", "Login successful");
        navigate("/");
      } else {
        handleSnackbarOpen("error", "Invalid email or password");
      }
    } catch (error) {
      console.error("Error during login:", error);
      handleSnackbarOpen(
        "error",
        "An error occurred during login. Please try again."
      );
    }
  };

  useEffect(() => {
    if (isAuthenticated) {
      navigate("/");
    }
  }, [isAuthenticated, navigate]);

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

      <Paper elevation={3} sx={{ padding: "40px", width: "800px" }}>
        <Typography
          variant="h1"
          style={{ fontWeight: "bold" }}
          textAlign={"left"}
          marginTop={"100px"}
          marginLeft={"60px"}
        >
          Let us be protected by the
          <div style={{ color: colors.greenAccent[500] }}>third eye!</div>
          <Typography
            variant="h5"
            margin={"20px"}
            fontStyle={"inherit"}
            color={colors.primary[100]}
          >
            Sign into Trinetra and uncover the magic that awaits.
          </Typography>
        </Typography>

        <form onSubmit={(e) => onSubmit(e)}>
          <TextField
            name="email"
            label="Email"
            placeholder="Email"
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
            value={email}
            onChange={(e) => onChange(e)}
            required
          />
          <TextField
            name="password"
            label="Password"
            placeholder="Password"
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
            value={password}
            onChange={(e) => onChange(e)}
          />
          <Grid
            container
            justifyContent="left"
            style={{ marginTop: "1%", marginLeft: "70px" }}
          >
            <FormControlLabel
              control={
                <Checkbox
                  control={
                    <Checkbox style={{ color: colors.greenAccent[500] }} />
                  }
                  label="Remember Password"
                />
              }
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
              component={Link}
              to="/reset-password"
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
            disabled={loading}
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
            <Typography
              variant="h5"
              margin="30px"
              marginLeft={"10%"}
              fontStyle={"inherit"}
              color={colors.primary[100]}
            >
              Don't have an account?
              <Typography
                variant="h6"
                style={{
                  cursor: "pointer",
                  color: colors.greenAccent[500],
                  marginLeft: "1%",
                  marginTop: "1%",
                }}
                component={Link}
                to="/signup"
              >
                Sign Up
              </Typography>
            </Typography>
          </Box>
        </form>
      </Paper>
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={2000}
        onClose={handleSnackbarClose}
        style={{ minWidth: "50px" }}
      >
        <MuiAlert
          elevation={6}
          variant="filled"
          severity={snackbarSeverity}
          onClose={handleSnackbarClose}
          style={{
            fontSize: "15px",
          }}
        >
          {snackbarMessage}
        </MuiAlert>
      </Snackbar>
    </Box>
  );
};

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { login })(LoginPage);
