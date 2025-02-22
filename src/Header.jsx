import { useState, useEffect } from "react";
import "./Header.css";

export function Header() {
  const [isOpen, setIsOpen] = useState(false);

  const handleClick = () => {
    setIsOpen((prev) => !prev);
  };

  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth >= 1024) {
        setIsOpen(false);
      }
    };

    window.addEventListener("resize", handleResize);
    return () => window.removeEventListener("resize", handleResize);
  }, []);

  return (
    <header className="py-4 px-4 shadow-md font-sans tracking-wide  fixed top-0 left-0 w-full bg-white z-[1000]">
      <div className="flex flex-wrap items-center justify-between w-full">
        <a href="#" className="max-sm:hidden">
          <img src="./public/Math.png " alt="logo" className="w-36" />
        </a>
        <a href="#" className="hidden max-sm:block">
          <img src="" alt="logo" className="w-9" />
        </a>

        {/* Menú principal */}
        <nav
          className={`lg:flex gap-x-5 max-lg:fixed max-lg:bg-white max-lg:w-3/4 max-lg:max-w-[400px] 
                      max-lg:top-0 max-lg:left-1/2 max-lg:-translate-x-1/2 max-lg:p-6 
                      max-lg:h-full max-lg:shadow-md max-lg:overflow-auto 
                      z-50 ${
                        isOpen
                          ? "max-lg:translate-y-0"
                          : "max-lg:-translate-y-full"
                      }`}
        >
          {/* Logo en el menú móvil */}
          <li className="mb-6 hidden max-lg:block">
            <a href="#">
              <img src="" alt="logo" className="w-36" />
            </a>
          </li>
          {["Home", "Chat", "Blog", "Board", "About", "Contact"].map(
            (item, index) => (
              <li
                key={index}
                className="max-lg:border-b border-gray-300 max-lg:py-3 px-3"
              >
                <a
                  href="#"
                  className="hover:text-[#007bff] text-gray-500 block font-semibold text-[15px]"
                >
                  {item}
                </a>
              </li>
            )
          )}
        </nav>

        {/* Botones de Login y Signup */}
        <div className="flex items-center space-x-4">
          <button className="px-4 py-2 text-sm rounded-full font-bold text-gray-500 border-2 bg-transparent hover:bg-gray-50 transition-all ease-in-out duration-300">
            Login
          </button>
          <button className="px-4 py-2 text-sm rounded-full font-bold text-white border-2 border-[#007bff] bg-[#007bff] transition-all ease-in-out duration-300 hover:bg-transparent hover:text-[#007bff]">
            Sign up
          </button>

          {/* Botón de menú móvil */}
          <button onClick={handleClick} className="lg:hidden">
            {isOpen ? (
              <svg
                className="w-7 h-7"
                fill="black"
                viewBox="0 0 320.591 320.591"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M30.391 318.583a30.37 30.37 0 0 1-21.56-7.288c-11.774-11.844-11.774-30.973 0-42.817L266.643 10.665c12.246-11.459 31.462-10.822 42.921 1.424 10.362 11.074 10.966 28.095 1.414 39.875L51.647 311.295a30.366 30.366 0 0 1-21.256 7.288z" />
                <path d="M287.9 318.583a30.37 30.37 0 0 1-21.257-8.806L8.83 51.963C-2.078 39.225-.595 20.055 12.143 9.146c11.369-9.736 28.136-9.736 39.504 0l259.331 257.813c12.243 11.462 12.876 30.679 1.414 42.922-.456.487-.927.958-1.414 1.414a30.368 30.368 0 0 1-23.078 7.288z" />
              </svg>
            ) : (
              <svg
                className="w-7 h-7"
                fill="black"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  fillRule="evenodd"
                  d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
                  clipRule="evenodd"
                ></path>
              </svg>
            )}
          </button>
        </div>
      </div>
    </header>
  );
}
