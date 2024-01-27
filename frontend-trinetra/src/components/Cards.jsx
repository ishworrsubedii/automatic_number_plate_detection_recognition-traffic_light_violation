import React from "react";
import { Box, Card, CardContent, Typography, useTheme } from "@mui/material";
import { tokens } from "../theme";

const DashboardCard = ({ title, value, percentage, icon }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  return (
    <Card sx={{ flex: "1 0 auto", m: 2, borderRadius: 2 }}>
      <CardContent>
        <Box display="flex" alignItems="center" justifyContent="space-between">
          <Box>
            <Typography variant="h6" color={colors.primary[300]}>
              {title}
            </Typography>
            <Typography variant="h4" color={colors.primary[100]}>
              {value}
            </Typography>
          </Box>
          <Box>
            {icon}
          </Box>
        </Box>
        <Box mt={2}>
          <Typography variant="h5" color={colors.primary[300]}>
            {percentage}
          </Typography>
        </Box>
      </CardContent>
    </Card>
  );
};

export default DashboardCard;