import React from "react";

import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

const rankingData = [
  {
    metric: "BM25",
    score: 0.79
  },
  {
    metric: "Hybrid LTR",
    score: 0.93
  }
];

const latencyData = [
  {
    system: "BM25",
    latency: 45
  },
  {
    system: "Hybrid",
    latency: 72
  }
];

export default function AnalyticsDashboard() {

  return (

    <div style={{
      padding: "20px"
    }}>

      <h1>
        Search Ranking Analytics Dashboard
      </h1>

      <h2>
        NDCG@10 Comparison
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <BarChart data={rankingData}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="metric" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="score" />

        </BarChart>

      </ResponsiveContainer>

      <h2 style={{
        marginTop: "50px"
      }}>
        Retrieval Latency
      </h2>

      <ResponsiveContainer
        width="100%"
        height={300}
      >

        <BarChart data={latencyData}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="system" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="latency" />

        </BarChart>

      </ResponsiveContainer>

    </div>
  );
}