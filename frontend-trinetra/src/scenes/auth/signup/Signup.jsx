import React, { useState } from "react";
import {
  Box,
  Paper,
  Typography,
  TextField,
  Button,
  useTheme,
  Checkbox,
  FormControlLabel,
  Grid,
} from "@mui/material";
import { tokens } from "../../../theme";
import trinetralogo from "../../../assets/trinetra.svg";

import { connect } from "react-redux";
import { signup } from "../../../actions/auth/auth";
import { useNavigate, Link } from "react-router-dom";

import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";

const SignupPage = ({ signup, isAuthenticated }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const navigate = useNavigate();

  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarSeverity, setSnackbarSeverity] = useState("success");
  const [snackbarMessage, setSnackbarMessage] = useState("");

  const handleSnackbarOpen = (severity, message) => {
    setSnackbarSeverity(severity);
    setSnackbarMessage(message);
    setSnackbarOpen(true);
  };

  const handleSnackbarClose = () => {
    setSnackbarOpen(false);
  };

  const containerStyle = {
    display: "flex",
    justifyContent: "left",
    height: "100vh",
    width: "1000px",
  };

  const [loading, setLoading] = useState(false);

  const [formData, setFormData] = useState({
    first_name: "",
    last_name: "",
    email: "",
    password: "",
    re_password: "",
  });

  const { first_name, last_name, email, password, re_password } = formData;

  const onChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = async (e) => {
    e.preventDefault();

    if (password === re_password) {
      setLoading(true);

      try {
        await signup(first_name, last_name, email, password, re_password);
        handleSnackbarOpen("success", "Account created successfully. Please login.");
        navigate("/login");
      } catch (error) {
        handleSnackbarOpen("error", "Signup failed. Please try again.");
      } finally {
        setLoading(false);
      }
    } else {
      handleSnackbarOpen("error", "Passwords do not match.");
    }
  };

  if (isAuthenticated) {
    navigate("/");
  }

  return (
    <Box sx={containerStyle}>
      <Paper elevation={3} sx={{ padding: "40px", width: "800px" }}>
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
        <Typography
          variant="h1"
          style={{ fontWeight: "bold" }}
          textAlign={"left"}
          marginTop={"100px"}
          marginLeft={"60px"}
        >
          Sign up to become the part of{" "}
          <span style={{ color: colors.greenAccent[500] }}>third eye!</span>
        </Typography>

        <Typography
          variant="h5"
          margin="30px"
          marginLeft={"10%"}
          fontStyle={"inherit"}
          color={colors.primary[100]}
        >
          Join Trinetra and experience the magic firsthand.
        </Typography>
        <form
          style={{
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            width: "90%",
          }}
          onSubmit={onSubmit}
        >
          <Grid
            container
            spacing={2}
            sx={{ marginTop: "20px", marginLeft: "60px" }}
          >
            <Grid item xs={6}>
              <TextField
                label="First Name"
                type="text"
                variant="outlined"
                fullWidth
                value={first_name}
                name="first_name"
                onChange={(e) => onChange(e)}
                required
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                label="Last Name"
                type="text"
                variant="outlined"
                fullWidth
                value={last_name}
                name="last_name"
                onChange={(e) => onChange(e)}
                required
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                label="Email"
                type="email"
                variant="outlined"
                fullWidth
                value={email}
                name="email"
                onChange={(e) => onChange(e)}
                required
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                label="Password"
                type="password"
                variant="outlined"
                fullWidth
                value={password}
                name="password"
                onChange={(e) => onChange(e)}
                minLength="8"
                required
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                label="Retype Password"
                type="password"
                variant="outlined"
                fullWidth
                value={re_password}
                name="re_password"
                onChange={(e) => onChange(e)}
                minLength="8"
                required
              />
            </Grid>
          </Grid>
          <Grid
            container
            alignItems="center"
            justifyContent="flex-start"
            sx={{ marginTop: "30px", marginLeft: "90px" }}
          >
            <Grid item>
              <FormControlLabel
                control={
                  <Checkbox style={{ color: colors.whiteAccent[500] }} />
                }
                label="I agree with"
                required
              />
            </Grid>
            <Grid item>
              <Link to="/termsandconditions" style={{ textDecoration: "none" }}>
                <Typography variant="h6" color={colors.greenAccent[500]}>
                  Terms and conditions
                </Typography>
              </Link>
            </Grid>
          </Grid>

          <Button
            type="submit"
            variant="contained"
            color="primary"
            sx={{
              backgroundColor: colors.greenAccent[500],
              color: colors.primary[500],
              marginTop: "5%",
              marginLeft: "30%",
              height: "5%",
              width: "50%",
              fontSize: "18px",
            }}
            disabled={loading}
          >
            <Typography style={{ fontWeight: "bold" }}>SIGN UP</Typography>
          </Button>
        </form>
        <Typography
          variant="h5"
          margin="30px"
          marginLeft={"10%"}
          fontStyle={"inherit"}
          color={colors.primary[100]}
        >
          Already have an account?
          <Typography
            variant="h6"
            style={{
              cursor: "pointer",
              color: colors.greenAccent[500],
              marginLeft: "1%",
              marginTop: "1%",
            }}
            component={Link}
            to="/login"
          >
            Login
          </Typography>
        </Typography>
      </Paper>
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={6000}
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

export default connect(mapStateToProps, { signup })(SignupPage);
