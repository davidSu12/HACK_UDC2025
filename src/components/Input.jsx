export function Input({ children, inputType }) {
  return (
    <div className="flex flex-col justify-items-center">
      <input type={inputType} className="" name="name" id="id" required />
      <label htmlFor="id" className="">
        {children}
      </label>
    </div>
  );
}
