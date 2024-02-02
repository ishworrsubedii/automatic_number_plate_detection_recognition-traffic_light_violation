import React, { useState } from "react";
import { Box, Paper, Typography, Button, useTheme } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { connect } from "react-redux";
import { verify } from "../../../actions/auth";
import { tokens } from "../../../theme";
import trinetralogo from "../../../assets/trinetra.svg";

const Accountactivation = (verify, match) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const [verified, setVerified] = useState(false);
  const navigate = useNavigate();

  const verify_account = (e) => {
    const uid = match.params.uid;
    const token = match.params.token;

    verify(uid, token);
    setVerified(true);
  };

  if (verified) {
    navigate("/");
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
          type="submit"
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

  // return(
  //     <div className='container'>
  //     <div
  //         className='d-flex flex-column justify-content-center align-items-center'
  //         style={{ marginTop: '200px' }}
  //     >
  //         <h1>Verify your Account:</h1>
  //         <button
  //             onClick={verify_account}
  //             style={{ marginTop: '50px' }}
  //             type='button'
  //             className='btn btn-primary'
  //         >
  //             Verify
  //         </button>
  //     </div>
  // </div>
  // );
};

export default connect(null, { verify })(Accountactivation);
