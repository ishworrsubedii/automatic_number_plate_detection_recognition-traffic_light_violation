import React from "react";
import {
  Box,
  Card,
  useTheme,
  IconButton,
  Divider,
  Typography,
} from "@mui/material";
import Header from "../../components/Header.jsx";

import { tokens } from "../../theme";
import TrendingDownIcon from "@mui/icons-material/TrendingDown";
import TrendingUpIcon from "@mui/icons-material/TrendingUp";

import DashboardCard from "../../components/Cards.jsx";
import BarChart from "../visualization/bar/Barchart.jsx";
import PieChart from "../visualization/pie/PieCharts.jsx";
import Linechart from "../visualization/line/Linecharts.jsx";
import BarchartTrafficRuleViolation from "../visualization/bar/BarchartViolation.jsx";

import ChartCard from "../../components/ChartCard.jsx";
import CustomFooter from "../global/Footer.jsx";

const Dashboard = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  return (
    <Box>

      <Box>
        <Box margin="20px">
          <Box
            display="flex"
            justifyContent={"space-between"}
            alignContent={"center"}
          >
            <Header
              title="DASHBOARD"
              subtitle="Welcome to your dashboard"
            ></Header>
          </Box>
        </Box>
        <Box
          display={"flex"}
          flexDirection={"row"}
          flexWrap="wrap"
          justifyContent="space-around"
        >
          <DashboardCard
            title="Total Vehicles Detected"
            value="721k"
            percentage="+11.01%"
            icon={<TrendingUpIcon />}
          />
          <DashboardCard
            title="Number Plate Recognized"
            value="367k"
            percentage="-0.01%"
            icon={<TrendingDownIcon />}
          />
          <DashboardCard
            title="Over Speed"
            value="1,156"
            percentage="+15.03%"
            icon={<TrendingUpIcon />}
          />
          <DashboardCard
            title="Total Vehicles Detected"
            value="239k"
            percentage="+6.08%"
            icon={<TrendingUpIcon />}
          />
        </Box>
      </Box>
      <Box sx={{ p: theme.spacing(3) }}>
      </Box>
      <Box display={'flex'} flexDirection={'row'}>
        <ChartCard title="Speed History" subtitle="Speed info" size={{ width: '900px', height: '400px' }}>
          <Linechart />

        </ChartCard>
        <ChartCard title="Traffic by Location" subtitle="Location info" size={{ width: '600px', height: '400px' }}>
        <BarchartTrafficRuleViolation />


        </ChartCard>
      </Box>


      <Box sx={{ p: theme.spacing(3) }}>
      </Box>

      <ChartCard title="Traffic by Location" subtitle="Location info" size={{ width: '100%', height: '400px' }}>
        <PieChart />
      </ChartCard>



      <Box sx={{ p: theme.spacing(3) }}>
        <ChartCard title="Violation" subtitle="Violation Reports" size={{ width: '100%', height: '400px' }}>
          <BarChart />
        </ChartCard>

      </Box>






      <div
        style={{
          bottom: 0,
          width: "100%",
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
        }}>
        <CustomFooter />

      </div>

    </Box>

  );
};

export default Dashboard;
