import React, { useEffect, useState } from "react";

import {
BarChart,
Bar,
XAxis,
YAxis,
Tooltip,
CartesianGrid,
ResponsiveContainer,
} from "recharts";

function AnalyticsPage() {

const [analytics, setAnalytics] = useState({
top_queries: {},
top_clicked_docs: {},
});

const API_URL =
"https://learning-to-rank-search-engine.onrender.com";

useEffect(() => {

```
const loadAnalytics = () => {

  fetch(
    `${API_URL}/analytics?t=${Date.now()}`
  )
    .then((res) => res.json())
    .then((data) => setAnalytics(data))
    .catch(console.error);

};

loadAnalytics();
```

}, []);

const queryData = Object.entries(
analytics.top_queries
).map(([query, count]) => ({
query,
count,
}));

const docData = Object.entries(
analytics.top_clicked_docs
).map(([title, clicks]) => ({
title:
title.length > 20
? title.substring(0, 20) + "..."
: title,
clicks,
}));

return (
<div
style={{
maxWidth: "1200px",
margin: "0 auto",
padding: "40px",
fontFamily: "Arial",
}}
> <h1>
📊 Search Analytics Dashboard </h1>

```
  <div
    style={{
      display: "flex",
      gap: "20px",
      marginBottom: "30px",
    }}
  >
    <div
      style={{
        flex: 1,
        padding: "20px",
        borderRadius: "12px",
        backgroundColor: "#eef2ff",
      }}
    >
      <h3>Total Queries</h3>

      <h2>
        {
          queryData.reduce(
            (sum, item) =>
              sum + item.count,
            0
          )
        }
      </h2>
    </div>

    <div
      style={{
        flex: 1,
        padding: "20px",
        borderRadius: "12px",
        backgroundColor: "#f0fdf4",
      }}
    >
      <h3>
        Clicked Documents
      </h3>

      <h2>
        {
          docData.reduce(
            (sum, item) =>
              sum + item.clicks,
            0
          )
        }
      </h2>
    </div>
  </div>

  <div
    style={{
      backgroundColor: "#fff",
      padding: "20px",
      borderRadius: "12px",
      boxShadow:
        "0 2px 8px rgba(0,0,0,0.1)",
      marginBottom: "30px",
    }}
  >
    <h2>📊 Top Queries</h2>

    <ResponsiveContainer
      width="100%"
      height={350}
    >
      <BarChart
        data={queryData}
      >
        <CartesianGrid strokeDasharray="3 3" />

        <XAxis
          dataKey="query"
          angle={-30}
          textAnchor="end"
          interval={0}
          height={100}
          tick={{
            fontSize: 12,
          }}
        />

        <YAxis />

        <Tooltip />

        <Bar
          dataKey="count"
        />
      </BarChart>
    </ResponsiveContainer>
  </div>

  <div
    style={{
      backgroundColor: "#fff",
      padding: "20px",
      borderRadius: "12px",
      boxShadow:
        "0 2px 8px rgba(0,0,0,0.1)",
    }}
  >
    <h2>
      📈 Most Clicked Documents
    </h2>

    <ResponsiveContainer
      width="100%"
      height={500}
    >
      <BarChart
        layout="vertical"
        data={docData}
        margin={{
          top: 20,
          right: 30,
          left: 120,
          bottom: 20,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />

        <XAxis
          type="number"
        />

        <YAxis
          type="category"
          dataKey="title"
          width={220}
          tick={{
            fontSize: 12,
          }}
        />

        <Tooltip />

        <Bar
          dataKey="clicks"
        />
      </BarChart>
    </ResponsiveContainer>
  </div>
</div>
```

);
}

export default AnalyticsPage;
