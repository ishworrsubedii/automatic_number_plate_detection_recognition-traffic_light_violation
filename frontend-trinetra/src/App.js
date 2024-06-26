import { useState, useEffect } from "react";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { ColorModeContext, useMode } from "./theme";
import { Routes, Route } from "react-router-dom";
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
import SignupPage from "./scenes/auth/signup/Signup";
import Forgotpassword from "./scenes/auth/forgotpassword/Forgotpassword";
import Forgotpasswordconfirm from "./scenes/auth/resetpassword/Forgotpasswordconfirm";
import Accountactivation from "./scenes/auth/accountactivation/Accountactivation";

import Termandconditions from "./scenes/termsandconditions/Termandcondition";
import WeaponDetectionService from "./scenes/weapon/WeaponDetection";

import { Provider, connect } from "react-redux";

import store from "./store";
import { checkAuthenticated, load_user } from "./actions/auth/auth";

const App = ({ isAuthenticated, checkAuthenticated, load_user }) => {
  const [theme, colorMode] = useMode();
  const [isSidebar, setIsSidebar] = useState(true);
  useEffect(() => {
    checkAuthenticated();
  }, [checkAuthenticated]);

  useEffect(() => {
    load_user();
  }, [load_user]);
  return (
    <Provider store={store}>
      <ColorModeContext.Provider value={colorMode}>
        <ThemeProvider theme={theme}>
          <CssBaseline />

          {isAuthenticated ? (
            <div className="app">
              {<Sidebar isSidebar={isSidebar} />}

              <main className="content">
                {<Topbar setIsSidebar={setIsSidebar} />}

                <Routes>
                  <Route path="/" element={<Dashboard />} />
                  <Route path="/server-status" element={<ServerStatus />} />
                  <Route path="/overview" element={<Overview />} />
                  <Route path="/projects" element={<Project />} />
                  <Route path="/server" element={<Server />} />
                  <Route path="/alpr" element={<Alpr />} />
                  <Route path="/speedtest" element={<Speed />} />
                  <Route
                    path="/violation"
                    element={<TrafficLightViolation />}
                  />
                  <Route path="/user-profile" element={<UserProfile />} />
                  <Route path="/account" element={<Account />} />
                  <Route path="/corporate" element={<Corporate />} />
                  <Route path="/blog" element={<Blog />} />
                  <Route path="/cameralist" element={<CameraList />} />
                  <Route path="/notification" element={<Notification />} />
                  <Route
                    path="/weapon-detection"
                    element={<WeaponDetectionService />}
                  />
                </Routes>
              </main>
            </div>
          ) : (
            <Routes>
              <Route path="/login" element={<LoginPage />} />
              <Route path="/signup" element={<SignupPage />} />
              <Route path="/reset-password" element={<Forgotpassword />} />
              <Route
                path="/password/reset/confirm/:uid/:token"
                element={<Forgotpasswordconfirm />}
              />
              <Route
                path="/activate/:uid/:token"
                element={<Accountactivation />}
              />
              <Route
                path="/termsandconditions"
                element={<Termandconditions />}
              />
            </Routes>
          )}
        </ThemeProvider>
      </ColorModeContext.Provider>
    </Provider>
  );
};

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { checkAuthenticated, load_user })(App);
