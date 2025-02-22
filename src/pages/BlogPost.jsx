import { Header } from "../components/Header.jsx";
import BlogCard from "../components/BlogCard.jsx";
import { Footer } from "../components/Footer.jsx";

export function BlogPost() {
  return (
    <>
      <Header />
      <div>
        <main className="w-3/3 bg-blue-400 p-4">
          <h2 className="mb-3 text-4xl font-bold text-center">Blogs</h2>
          <BlogCard />
        </main>
        <Footer />
      </div>
    </>
  );
}
