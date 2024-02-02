import React, { useState } from "react";
import { Box, Paper, Typography, Button, useTheme } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { connect } from "react-redux";
import { verify } from "../../../actions/auth";
import { tokens } from "../../../theme";
import trinetralogo from "../../../assets/trinetra.svg";
import { useParams } from 'react-router-dom';


const Accountactivation = ({ verify, match }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const [verified, setVerified] = useState(false);
  const navigate = useNavigate();
  const { uid, token } = useParams();

  const verify_account = (e) => {
    verify(uid, token);
    setVerified(true);
   


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
          Verify your Account to further proceed!
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
          onClick={verify_account}
        >
          Verify Account
        </Button>
      </Paper>
    </Box>
  );


};

export default connect(null, { verify })(Accountactivation);
