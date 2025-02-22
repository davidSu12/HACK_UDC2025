import { BlogEntries } from "./pages/BlogEntries";
import { Chat } from "./pages/Chat";
import { Error } from "./pages/Error";
import { HomeStudent } from "./pages/Student/HomeStudent";
import { HomeTeacher } from "./pages/Teacher/HomeTeacher";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

export function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomeStudent />} />
        <Route path="/contact" element={<BlogEntries />} />
        <Route path="*" element={<Error />} />{" "}
        {/* Página por defecto si no encuentra la ruta */}
      </Routes>
    </Router>
  );
}
