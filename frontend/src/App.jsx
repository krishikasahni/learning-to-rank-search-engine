import React from "react";
import {
  BrowserRouter,
  Routes,
  Route,
  Link,
} from "react-router-dom";

import SearchPage from "./pages/SearchPage";
import AnalyticsPage from "./pages/AnalyticsPage";

function App() {
  return (
    <BrowserRouter>
      <div
        style={{
          minHeight: "100vh",
          display: "flex",
          flexDirection: "column",
        }}
      >
        {/* Navbar */}
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            alignItems: "center",
            padding: "20px 40px",
            borderBottom: "1px solid #ddd",
            backgroundColor: "#f8f9fa",
          }}
        >
          <h2
            style={{
              margin: 0,
            }}
          >
            AI Search Engine
          </h2>

          <div>
            <Link
              to="/"
              style={{
                marginRight: "20px",
                textDecoration: "none",
                fontWeight: "bold",
                color: "#333",
              }}
            >
              Search
            </Link>

            <Link
              to="/analytics"
              style={{
                textDecoration: "none",
                fontWeight: "bold",
                color: "#333",
              }}
            >
              Analytics
            </Link>
          </div>
        </div>

        {/* Main Content */}
        <div style={{ flex: 1 }}>
          <Routes>
            <Route
              path="/"
              element={<SearchPage />}
            />

            <Route
              path="/analytics"
              element={<AnalyticsPage />}
            />
          </Routes>
        </div>

        {/* Footer */}
        <footer
          style={{
            textAlign: "center",
            padding: "20px",
            borderTop: "1px solid #ddd",
            backgroundColor: "#f8f9fa",
            marginTop: "30px",
          }}
        >
          <strong>
            Hybrid Learning-to-Rank Search Engine
          </strong>
        </footer>
      </div>
    </BrowserRouter>
  );
}

export default App;