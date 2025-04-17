import "./App.css";
import React from "./assets/react.png";
export default function App() {
  return (
      <div className="webgen">
        <h1>Webgen + React</h1>
        <div className="img">
          <img src={React} alt="" width="200px" />
        </div>
        <div className="react-con">
            <a className="react" href="https://react.dev/" target="_blank">React</a>
        </div>
        <div className="desc">
          <h5>
            Thank you for using my webgen, honestly, webgen is only made for fun
            projects. If you want to <br /> continue using it, please use this
            tool. Later there will be the latest update from this webgen tool{" "}
            <br /> and don't forget to visit my github profile. Thank you.
          </h5>
        </div>
        <div className="github">
          <a href="https://github.com/zen-Hikari" target="_blank">
            My Github
          </a>
        </div>
      </div>
  );
}
