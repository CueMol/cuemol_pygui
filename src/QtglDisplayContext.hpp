// -*-Mode: C++;-*-
//
//  Qt GL display context implementation
//

#ifndef QTGL_DISPLAY_CONTEXT_HPP_
#define QTGL_DISPLAY_CONTEXT_HPP_

#include <sysdep/OglDisplayContext.hpp>
#include "QtglView.hpp"

namespace qtgui {

  class QtglDisplayContext : public sysdep::OglDisplayContext
  {
  private:

    //QtglView *m_pTargetView;

    /// QGLContext
    void *m_pCtxt;

  public:
    // QtglDisplayContext(int sceneid, QtglView *pView, void *pCtxt);
    QtglDisplayContext();

    virtual ~QtglDisplayContext();

    virtual bool setCurrent();
    virtual bool isCurrent() const;

    //virtual qsys::View *getTargetView() const {
    //return m_pTargetView;
    //}

    ///////////////
    // system dependent methods
    
    bool attach(void *pCtxt);

    // HGLRC getHGLRC() const { return m_hGlrc; }
  };

}

#endif
