import React, { useState } from "react";
import { Box, Paper, Typography, Button, useTheme } from "@mui/material";
import { useNavigate, useParams } from "react-router-dom";
import { connect } from "react-redux";
import { verify } from "../../../actions/auth/auth";
import { tokens } from "../../../theme";
import trinetralogo from "../../../assets/trinetra.svg";

import Snackbar from "@mui/material/Snackbar";
import MuiAlert from "@mui/material/Alert";

const AccountActivation = ({ verify }) => {
  const theme = useTheme();
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

  const [verified, setVerified] = useState(false);
  const navigate = useNavigate();
  const { uid, token } = useParams();

  const verifyAccount = () => {
    verify(uid, token)
      .then((result) => {
        if (result === "success") {
          handleSnackbarOpen("success", "Account verified successfully.");
          setVerified(true);
        } else {
          handleSnackbarOpen(
            "error",
            "Account verification failed. Please try again."
          );
        }
      })
      .catch(() => {
        handleSnackbarOpen("error", "An error occurred during verification.");
      });
  };

  if (verified) {
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
          variant="h2"
          style={{ fontWeight: "bold" }}
          textAlign={"left"}
          marginTop={"30%"}
          marginLeft={"60px"}
        >
          Verify your Account to proceed further!
        </Typography>

        <Button
          type="button"
          variant="contained"
          style={{
            borderRadius: 50,
            width: "40%",
            marginTop: "10%",
            marginLeft: "30%",
            backgroundColor: colors.greenAccent[500],
            color: "black",
          }}
          disabled={loading}
          onClick={verifyAccount}
        >
          Verify Account
        </Button>
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

export default connect(null, { verify })(AccountActivation);
