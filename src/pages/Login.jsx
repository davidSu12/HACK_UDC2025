import { Header } from "../Header";
import { Input } from "../components/Input";
export function Login() {
  return (
    <>
      <Header />
      <div className="flex lg:flex-row lg:gap-10 flex-col justify-items-center me w-full">
        <div className="flex flex-col gap-3 ">
          <img className="max-h-20 max-v-20" src="./public/Math.png" alt="" />
        </div>
        <div>
          <form action="">
            <Input inputType="email">Email</Input>
            <Input inputType="password">Password</Input>

            <div className="m-4 w-full border-t-white border-t-2"></div>
          </form>
        </div>
      </div>
    </>
  );
}
