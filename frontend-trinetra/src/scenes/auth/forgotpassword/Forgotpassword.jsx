import React, { useState } from "react";
import {
  Box,
  Paper,
  Typography,
  TextField,
  Button,
  useTheme,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import { connect } from "react-redux";
import { reset_password } from "../../../actions/auth/auth";
import { tokens } from "../../../theme";

import InputAdornment from "@mui/material/InputAdornment";
import EmailIcon from "@mui/icons-material/Email";
import trinetralogo from "../../../assets/trinetra.svg";

import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";

const ForgotPassword = ({ reset_password }) => {
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

  const [requestSent, setRequestSent] = useState(false);
  const [formData, setFormData] = useState({
    email: "",
  });

  const { email } = formData;

  const onChange = (e) => setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = async (e) => {
    e.preventDefault();

    try {
      const resetResult = await reset_password(email);

      if (resetResult === "success") {
        handleSnackbarOpen("success", "Password reset email sent successfully.");
        setRequestSent(true);
      } else {
        handleSnackbarOpen("error", "Password reset failed. Please try again.");
      }
    } catch (error) {
      handleSnackbarOpen("error", "An error occurred during password reset.");
    }
  };

  if (requestSent) {
    navigate("/login");
  }

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
        >
          Forgot your password?
          <div style={{ color: colors.greenAccent[500] }}>No worries!</div>
          <Typography
            variant="h5"
            margin={"20px"}
            fontStyle={"inherit"}
            color={colors.primary[100]}
            value={email}
          >
            Enter your email to reset your password.
          </Typography>
        </Typography>

        <form onSubmit={(e) => onSubmit(e)}>
          <TextField
            label="Email"
            type="email"
            variant="outlined"
            value={email}
            name="email"
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <EmailIcon
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
            onChange={(e) => onChange(e)}
            required
          />
          <Button
            type="submit"
            variant="contained"
            style={{
              borderRadius: 50,
              width: "80%",
              marginTop: "20px",
              marginLeft: "60px",
              backgroundColor: colors.greenAccent[500],
              color: "black",
            }}
            disabled={loading}
          >
            Reset Password
          </Button>
        </form>
      </Paper>
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={6000}
        onClose={handleSnackbarClose}
        anchorOrigin={{ vertical: "top", horizontal: "center" }}
      >
        <MuiAlert
          elevation={6}
          variant="filled"
          severity={snackbarSeverity}
          onClose={handleSnackbarClose}
        >
          {snackbarMessage}
        </MuiAlert>
      </Snackbar>
    </Box>
  );
};

export default connect(null, { reset_password })(ForgotPassword);
