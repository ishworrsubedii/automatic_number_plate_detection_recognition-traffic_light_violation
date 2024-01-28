import React from 'react';
import PropTypes from 'prop-types';
import { Box, Typography,useTheme } from '@mui/material';
import { tokens } from '../theme';


const CameraInfo = ({ isLoading }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);


  return (
    <Box fontStyle={colors.primary[100]}>
      <Typography variant="h3">Camera Info</Typography>
      {isLoading ? (
        <Typography variant="body1">Camera information is loading...</Typography>
      ) : (
        <Typography variant="h7" >Camera information is still loading...</Typography>)}
    </Box>
  );
};

CameraInfo.propTypes = {
  isLoading: PropTypes.bool.isRequired,
};

export default CameraInfo;