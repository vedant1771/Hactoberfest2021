;; Single bick break at - Metrix PB
 
(defun C:Bsp ( / Ent Pt Tmp osm)
(setq Tmp (getvar "cmdecho"))
(setvar "Cmdecho" 0)
(setq osm (getvar "osmode")) ;store osnap settings
(setvar "osmode" 683)
 
(setq Pt (getpoint "\nspecify point break point: "))
(setq Ent Pt)
(command ".break" Ent "F" "none" Pt "none" Pt)
 
(setvar "Cmdecho" Tmp)
(setvar "osmode" osm) ;RESTORE OSNAP 
(princ)
)