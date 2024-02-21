import type { FC } from 'react'

type LogoSiteProps = {
  className?: string
}
const LogoSite: FC<LogoSiteProps> = ({
  className,
}) => {
  console.log('LogoSiteProps', className)
  return (
    <img
      src='/logo/logo-site.png'
      className={`block asdasd w-auto h-10 ${className}`}
      alt='logo'
    />
  )
}

export default LogoSite
