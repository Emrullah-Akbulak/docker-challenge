import { useCallback, useEffect, useState } from "react";
import {
  CartesianGrid,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import styles from "../assets/Home/home.module.css";

type HeatData = {
  id: number;
  firstSensor: number;
  secondSensor: number;
  thirdSensor: number;
  createdAt: string;
  updatedAt: string;
};

function Home() {
  const [heatData, setHeatData] = useState<HeatData[]>([]);

  const getData = useCallback(async () => {
    const req = await fetch("http://localhost:8000/api/heat/?limit=30").catch(
      () => null
    );

    if (!req || req.status !== 200) {
      return;
    }

    const data: HeatData[] = await req.json();

    const mapped = data.map((d) => {
      return {
        ...d,
        createdAt: new Date(d.createdAt).toLocaleTimeString(),
      };
    });

    setHeatData(() => mapped);
  }, [setHeatData]);

  useEffect(() => {
    getData();
    const interval = setInterval(getData, 5000);

    return () => {
      clearInterval(interval);
    };
  }, [getData]);

  return (
    <div className={styles.homeWrapper}>
      <ResponsiveContainer height="80%" width="90%">
        <LineChart
          title="Heat Graph"
          className={styles.lineChart}
          data={heatData}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="5 5" />
          <XAxis padding={{ right: 35 }} dataKey="createdAt" name="Date" />
          <YAxis name="Temprature" />
          <Tooltip />
          <Line
            type="monotone"
            dataKey="firstSensor"
            name="Sensor 1"
            stroke="#8884d8"
            isAnimationActive={false}
          />
          <Line
            type="monotone"
            name="Sensor 2"
            dataKey="secondSensor"
            stroke="#82ca9d"
            isAnimationActive={false}
          />
          <Line
            type="monotone"
            name="Sensor 3"
            dataKey="thirdSensor"
            stroke="#555555"
            isAnimationActive={false}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}
export default Home;
