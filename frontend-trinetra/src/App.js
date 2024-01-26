import { useState, useEffect } from "react";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { ColorModeContext, useMode } from "./theme";

import { Routes, Route, Navigate, useNavigate } from "react-router-dom";
import Topbar from "./scenes/global/Topbar";
import Sidebar from "./scenes/global/Sidebar";
import Dashboard from "./scenes/dashboard/Dashboard";
import ServerStatus from "./scenes/server/Server";
import Overview from "./scenes/overview/Overview";
import Project from "./scenes/projects/ProjectList";
import Server from "./scenes/server/Server";
import Alpr from "./scenes/alpr/Alpr";
import Speed from "./scenes/speed/Speed";
import TrafficLightViolation from "./scenes/violation/TrafficLight";
import UserProfile from "./scenes/userprofile/Userprofile";
import Account from "./scenes/account/Account";
import Corporate from "./scenes/corporate/Corporate";
import Blog from "./scenes/blog/Blog";
import CameraList from "./scenes/cameralist/CameraStatus";
import Notification from "./scenes/notification/Notification";

import LoginPage from "./scenes/auth/login/Login";
function App() {
  const [theme, colorMode] = useMode();
  const [isSidebar, setIsSidebar] = useState(true);
  const [isLoggedIn, setLoggedIn] = useState(false);
  const navigate = useNavigate();

  const handleLogin = () => {

    setLoggedIn(true);
    navigate("/");
  };

  useEffect(() => {
    if (!isLoggedIn) {
      navigate("/login");
    }
  }, [isLoggedIn, navigate]);

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          {isLoggedIn && <Sidebar isSidebar={isSidebar} />}
          <main className="content">
            {isLoggedIn && <Topbar setIsSidebar={setIsSidebar} />}
            <Routes>
              <Route
                path="/"
                element={isLoggedIn ? <Dashboard /> : <Navigate to="/login" />}
              />
              <Route
                path="/login"
                element={<LoginPage onLogin={handleLogin} />}
              />
              <Route path="/server-status" element={<ServerStatus />} />
              <Route path="/overview" element={<Overview />} />
              <Route path="/projects" element={<Project />} />
              <Route path="/server" element={<Server />} />
              <Route path="/alpr" element={<Alpr />} />
              <Route path="/speed" element={<Speed />} />
              <Route
                path="/traffic-light-violation"
                element={<TrafficLightViolation />}
              />
              <Route path="/user-profile" element={<UserProfile />} />
              <Route path="/account" element={<Account />} />
              <Route path="/corporate" element={<Corporate />} />
              <Route path="/blog" element={<Blog />} />
              <Route path="/camera-list" element={<CameraList />} />
              <Route path="/notification" element={<Notification />} />
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
